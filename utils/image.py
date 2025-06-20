import os
import uuid
import logging
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

logger = logs()

class ImageProcessingError(PhotoProError):
    pass

@dataclass
class ImageConfig:
    max_size: Tuple[int, int] = (1024, 1024)
    resampling_method: Image.Resampling = Image.Resampling.LANCZOS
    supported_formats: Tuple[str, ...] = ('JPEG', 'PNG', 'WEBP', 'TIFF', 'BMP')
    max_file_size_mb: int = 20
    quality: int = 95


class ImageValidator:
    
    def __init__(self, config: ImageConfig):
        self.config = config
    
    def validate_image_file(self, image_path: str) -> bool:
        """
        Validate image.
        
        Args:
            image_path (str): Path to the image file
            
        Returns:
            bool: True if valid, raises exception if invalid
            
        Raises:
            ImageProcessingError: If image is invalid
        """
        path = Path(image_path)
        
        # Check if file exists
        if not path.exists():
            raise ImageProcessingError(f"Image file not found: {image_path}")
        
        # Check file size
        file_size_mb = path.stat().st_size / (1024 * 1024)
        if file_size_mb > self.config.max_file_size_mb:
            raise ImageProcessingError(
                f"Image file too large: {file_size_mb:.2f}MB > {self.config.max_file_size_mb}MB"
            )
        
        # Validate image format
        try:
            with Image.open(image_path) as img:
                if img.format not in self.config.supported_formats:
                    raise ImageProcessingError(
                        f"Unsupported image format: {img.format}. "
                        f"Supported formats: {', '.join(self.config.supported_formats)}"
                    )
                
                # Check if image can be loaded
                img.verify()
                
        except Exception as e:
            if isinstance(e, ImageProcessingError):
                raise
            raise ImageProcessingError(f"Invalid image file: {str(e)}")
        
        return True



class ImageProcessor:    
    def __init__(self, config: ImageConfig):
        self.config = config
        self.validator = ImageValidator(config)
    
    def prepare_image(self, image_path: str) -> Image.Image:
        """
        Prepare image for processing by Gemini API.
        
        Args:
            image_path (str): Path to the image file
            
        Returns:
            Image.Image: Processed PIL Image object
            
        Raises:
            ImageProcessingError: If image processing fails
        """
        try:
            # Validate image
            self.validator.validate_image_file(image_path)
            
            # Open and process image
            with Image.open(image_path) as img:
                # Convert to RGB
                if img.mode != 'RGB':
                    img = img.convert('RGB')
                
                # Resize image
                if img.size[0] > self.config.max_size[0] or img.size[1] > self.config.max_size[1]:
                    img.thumbnail(self.config.max_size, self.config.resampling_method)
                    logger.info(f"Resized image to {img.size}")
                
                # Apply auto-orientation based on EXIF data
                img = ImageOps.exif_transpose(img)
                
                processed_img = img.copy()
                
            logger.info(f"Successfully prepared image: {image_path}")
            return processed_img
            
        except Exception as e:
            if isinstance(e, ImageProcessingError):
                raise
            raise ImageProcessingError(f"Failed to prepare image: {str(e)}")
    
    def save_enhanced_image(self, image: Image.Image, output_path: str) -> str:
        """
        Save enhanced image with optimized settings.
        
        Args:
            image (Image.Image): PIL Image to save
            output_path (str): Path where to save the image
            
        Returns:
            str: Path to saved image
            
        Raises:
            ImageProcessingError: If saving fails
        """
        try:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            
            
            save_kwargs = {
                'quality': self.config.quality,
                'optimize': True
            }
            
            if output_path.lower().endswith('.png'):
                save_kwargs['compress_level'] = 6
            elif output_path.lower().endswith('.webp'):
                save_kwargs['method'] = 6
            
            image.save(output_path, **save_kwargs)
            logger.info(f"Saved enhanced image to: {output_path}")
            
            return output_path
            
        except Exception as e:
            raise ImageProcessingError(f"Failed to save image: {str(e)}")

