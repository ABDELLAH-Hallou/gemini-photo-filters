import os
import uuid

from io import BytesIO
from pathlib import Path
from typing import Optional, Tuple, Dict, Any, List
from dataclasses import dataclass
from datetime import datetime

import numpy as np
from PIL import Image, ImageOps
from google import genai
from google.genai import types

from utils.handler import PhotoProError, logs
from utils.image import ImageConfig, ImageProcessingError, ImageProcessor
logger = logs()






@dataclass
class GeminiConfig:
    """Gemini API."""
    model_name: str = "gemini-2.0-flash-preview-image-generation"
    response_modalities: List[str] = None
    timeout_seconds: int = 60
    max_retries: int = 3
    
    def __post_init__(self):
        if self.response_modalities is None:
            self.response_modalities = ['TEXT', 'IMAGE']


class GeminiAPIError(PhotoProError):
    pass


class GeminiEnhancementEngine:    
    def __init__(self, api_key: str, gemini_config: GeminiConfig = None, image_config: ImageConfig = None):
        self.gemini_config = gemini_config or GeminiConfig()
        self.image_config = image_config or ImageConfig()
        self.image_processor = ImageProcessor(self.image_config)
        
        # Configure Gemini API
        try:
            self.client = genai.Client(api_key=api_key)
            logger.info("Gemini API configured successfully")
        except Exception as e:
            raise GeminiAPIError(f"Failed to configure Gemini API: {str(e)}")
    
    def enhance_image(self, image_path: str, prompt: str, output_dir: str = None) -> Dict[str, Any]:
        """
        Enhance an image using Gemini AI with the given prompt.
        
        Args:
            image_path (str): Path to the input image
            prompt (str): Enhancement prompt for Gemini
            output_dir (str, optional): Directory to save enhanced images
            
        Returns:
            Dict[str, Any]: Result containing enhanced image info and metadata
            
        Raises:
            ImageProcessingError: If image processing fails
            GeminiAPIError: If Gemini API call fails
        """
        start_time = datetime.now()
        session_id = str(uuid.uuid4())[:8]
        
        logger.info(f"Starting enhancement session {session_id} for image: {image_path}")
        
        try:
            # Prepare image
            processed_image = self.image_processor.prepare_image(image_path)
            
            if output_dir is None:
                output_dir = f"enhanced_images_{session_id}"
            
            Path(output_dir).mkdir(parents=True, exist_ok=True)
            
            response = self._call_gemini_api_with_retry(processed_image, prompt)
            
            # Process response
            result = self._process_gemini_response(response, output_dir, session_id)
            
            # Add metadata
            processing_time = (datetime.now() - start_time).total_seconds()
            result.update({
                'session_id': session_id,
                'original_image': image_path,
                'prompt': prompt,
                'processing_time_seconds': processing_time,
                'timestamp': datetime.now().isoformat()
            })
            
            logger.info(f"Enhancement completed successfully in {processing_time:.2f}s")
            return result
            
        except Exception as e:
            logger.error(f"Enhancement failed for session {session_id}: {str(e)}")
            if isinstance(e, (ImageProcessingError, GeminiAPIError)):
                raise
            raise PhotoProError(f"Unexpected error during enhancement: {str(e)}")
    
    def _call_gemini_api_with_retry(self, image: Image.Image, prompt: str) -> Any:
        """
        Call Gemini API with retry logic.
        
        Args:
            image (Image.Image): Processed image
            prompt (str): Enhancement prompt
            
        Returns:
            Gemini API response
            
        Raises:
            GeminiAPIError: If all retry attempts fail
        """
        last_exception = None
        
        for attempt in range(self.gemini_config.max_retries):
            try:
                logger.info(f"Calling Gemini API (attempt {attempt + 1}/{self.gemini_config.max_retries})")
                
                response = self.client.models.generate_content(
                    model=self.gemini_config.model_name,
                    contents=[(prompt,), image],
                    config=types.GenerateContentConfig(
                        response_modalities=self.gemini_config.response_modalities
                    )
                )
                
                if not response.candidates:
                    raise GeminiAPIError("No candidates in Gemini response")
                
                return response
                
            except Exception as e:
                last_exception = e
                logger.warning(f"Gemini API attempt {attempt + 1} failed: {str(e)}")
                
                if attempt < self.gemini_config.max_retries - 1:
                    import time
                    time.sleep(2 ** attempt)  
        
        raise GeminiAPIError(f"Gemini API failed after {self.gemini_config.max_retries} attempts: {str(last_exception)}")
    
    def _process_gemini_response(self, response: Any, output_dir: str, session_id: str) -> Dict[str, Any]:
        """
        Process Gemini API response and save results.
        
        Args:
            response: Gemini API response
            output_dir (str): Output directory
            session_id (str): Session identifier
            
        Returns:
            Dict[str, Any]: Processing results
            
        Raises:
            GeminiAPIError: If response processing fails
        """
        try:
            result = {
                'text_responses': [],
                'enhanced_images': [],
                'output_directory': output_dir
            }
            
            for part in response.candidates[0].content.parts:
                if part.text is not None:
                    result['text_responses'].append(part.text)
                    logger.info(f"Gemini text response: {part.text}")
                
                elif part.inline_data is not None:
                    enhanced_image = Image.open(BytesIO(part.inline_data.data))
                    
                    # Generate unique filename
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"enhanced_{session_id}_{timestamp}.png"
                    output_path = os.path.join(output_dir, filename)
                    
                    # Save enhanced image
                    saved_path = self.image_processor.save_enhanced_image(enhanced_image, output_path)
                    
                    # Add image info to result
                    image_info = {
                        'path': saved_path,
                        'filename': filename,
                        'size': enhanced_image.size,
                        'format': enhanced_image.format,
                        'mode': enhanced_image.mode
                    }
                    result['enhanced_images'].append(image_info)
                    
                    logger.info(f"Saved enhanced image: {saved_path}")
            
            if not result['enhanced_images'] and not result['text_responses']:
                raise GeminiAPIError("No usable content in Gemini response")
            
            return result
            
        except Exception as e:
            if isinstance(e, GeminiAPIError):
                raise
            raise GeminiAPIError(f"Failed to process Gemini response: {str(e)}")
