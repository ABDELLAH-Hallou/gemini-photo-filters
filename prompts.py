import random
from typing import Dict, List, Optional

class PhotoPromptSelector:
    """
    A class to randomly select photo enhancement prompts from different categories.
    Perfect for PhotoPro application to provide variety in image transformations.
    """
    
    def __init__(self):
        """Initialize the prompt selector with predefined categories and prompts."""
        self.prompts = {
            "quality_enhancement": [
                "Enhance this photo to professional photography standards by improving sharpness, optimizing exposure and contrast, correcting color balance, and reducing any noise while preserving the natural look and original composition.",#1
                
                "Transform this image into a high-definition, crisp photograph with perfect lighting balance, enhanced details in both shadows and highlights, and vibrant but natural colors that make it suitable for professional portfolio use.",#1
                
                "Improve this photo's visual impact by enhancing clarity and definition, optimizing the dynamic range to reveal details in dark and bright areas, and applying subtle color grading that makes the image more visually appealing while maintaining photographic realism."#2
            ],
            
            "artistic_style": [
                "Transform this photograph into a cinematic masterpiece with dramatic lighting reminiscent of film noir, enhanced contrast that creates mood and depth, and a color palette that evokes the golden age of Hollywood cinema.", # 0.5
                
                "Convert this image into a fine art photograph with the aesthetic of Ansel Adams - rich black and white tones, exceptional detail in textures, dramatic sky contrast, and the kind of composition that would belong in a museum gallery.",# 0
                
                "Reimagine this photo in the style of Renaissance painting with warm, golden lighting that creates depth and dimension, enhanced colors that have the richness of oil paint, and a composition that feels both classical and timeless." # 0.5
            ],
            
            "mood_atmosphere": [
                "Enhance this image to create a warm, nostalgic atmosphere by adding golden hour lighting effects, softening harsh shadows, enriching warm tones while cooling the highlights slightly, and creating a dreamy quality that evokes cherished memories.", #1
                
                "Transform this photo into a dramatic, powerful image with stormy sky effects, enhanced contrast that creates visual tension, cooler color temperatures that suggest mystery, and lighting that makes the subject appear heroic and commanding.",#1
                
                "Convert this photograph into a serene, peaceful scene by softening all harsh elements, creating gentle, diffused lighting that feels like early morning mist, enhancing greens and blues while muting aggressive colors, and adding a subtle ethereal quality."#0
            ],
            
            "portrait_enhancement": [
                "Enhance this portrait to professional headshot quality by smoothing skin texture while maintaining natural appearance, brightening and sharpening the eyes, optimizing facial lighting to be flattering, and ensuring the background complements rather than distracts from the subject.",#0
                
                "Transform this portrait into a high-end fashion photography style with perfect skin retouching, dramatic lighting that sculpts facial features, enhanced eye definition and lip color, and a polished look suitable for magazine publication.",#0
                
                "Improve this portrait by creating natural-looking skin enhancement, brightening the eyes to make them more engaging, optimizing the lighting to eliminate unflattering shadows, and ensuring the overall result looks professional yet authentic."#0
            ],
            
            "landscape_nature": [
                "Enhance this landscape to showcase nature's grandeur by intensifying the sky drama, enriching the colors of vegetation, improving the contrast between different landscape elements, and creating depth that draws viewers into the scene.",#
                
                "Transform this nature photograph into a breathtaking vista by enhancing the golden hour lighting, making the colors more saturated while keeping them natural, improving the clarity of distant elements, and creating a sense of scale that emphasizes the landscape's majesty.",#
                
                "Convert this outdoor scene into a calendar-worthy photograph by optimizing the lighting to create visual interest, enhancing the natural colors without making them artificial, improving the overall composition balance, and ensuring every element contributes to the scenic beauty."#
            ],
            
            "creative_artistic": [
                "Reimagine this photograph as a watercolor painting with soft, flowing edges, transparent color washes that blend naturally, artistic brush stroke textures, and the kind of delicate beauty that characterizes fine watercolor art.",#0.5
                
                "Transform this image into a vintage poster design with bold, simplified colors, enhanced contrast that creates graphic impact, slightly stylized elements that feel hand-crafted, and the timeless appeal of classic advertising art.",#1
                
                "Convert this photo into a digital art masterpiece with enhanced colors that border on surreal, lighting effects that create drama and atmosphere, textures that add artistic interest, and an overall aesthetic that bridges photography and digital art."#1
            ],
            
            "others":[
                "Apply a watercolor filter with soft edges and vibrant, but slightly muted colors to give the scenery a dreamy and impressionistic look",#0.5
                "Transform this image into a delicate watercolor painting, with soft edges and a dreamy, diffused appearance. The colors should be vibrant but slightly muted, creating an impressionistic feel",#1
                "Apply a bold oil painting filter, capturing the texture and depth of thick brushstrokes. The colors should be rich and vibrant, creating a sense of movement and energy in the scene.",#1
                "Transform this photograph into a timeless sketch, capturing the essence of the subject with simple lines and subtle shading. The lines should be clean and expressive, creating a sense of dynamism and elegance.",#1
                "Transform this image into a nostalgic vintage Polaroid, with faded edges, a slightly grainy texture, and warm, slightly desaturated colors. Capture the essence of a cherished memory.",#1
                "Give this image a futuristic cyberpunk vibe, using vibrant neon colors, glowing lines, and a sense of depth and detail. Emphasize the contrast between the dark and luminous elements, creating a captivating, almost otherworldly atmosphere.",#0.5
                "Apply a traditional Japanese woodblock print filter, using bold, flat colors, sharp lines, and subtle textures. Emulate the artistic style of a classic woodblock print, with a sense of elegance and simplicity.",#0.5
                "line art, black and white, minimalist, elegant lines, high contrast, 4k resolution",#1
                "watercolor art, vibrant colors, soft edges, painterly style, artistic interpretation, dreamy atmosphere, 4k resolution",#1
                
            ],
            "Pro":[
                "turn this photo into a sharp cinematic portrait of me standing in profile in the middle of a busy urban street, wearing a stylish dark blazer, moody lighting with soft shadows, 35mm film look. The background is motion-blurred with people walking fast, creating a dramatic contrast. Shallow depth of field, subject in razor-sharp focus. Shot in natural golden hour light, with rich contrast and cinematic color grading. Vertical photo, portrait orientation, 9:16.",#1
                "turn this photo into a luxurious rooftop portrait with skyline in the background. Maintain the original selfie’s face without any AI face modification. The subject is in a smart-casual outfit — open collar shirt, linen blazer, watch visible on wrist and black sunglasses. Sunset lighting casts soft golden tones across the skin. Behind, a modern city skyline fades into warm bokeh. Clean, editorial look with professional photography vibes. 4K clarity, vertical 9:16.",#1
                "turn this photo into a CREATE A HYPER-DETAILED GRAPHIC DESIGN FEATURING A STRIKING PORTRAIT OF A YOUNG MAN WITH THE SAME FACE AS UPLOADED] WITH A CONFIDENT DEMEANOUR. HIS HEAD IS ADORNED WITH VOLUMINOUS, ADDING TEXTURE AND DEPTH TO THE COMPOSITION. THE PORTRAIT IS RENDERED IN A HIGH-CONTRAST BLACK-AND-WHITE STYLE, STANDING OUT AGAINST THE MINIMALIST BACKGROUND. HIS EXPRESSION IS CALM YET DETERMINED, WITH ONE EYE PARTIALLY OBSCURED BY A BOLD RED RECTANGULAR OVERLAY THAT ADDS A MODERN, ARTISTIC FLAIR THE BACKGROUND IS A SMOOTH, TEXTURED GREY CANVAS, SERVING AS A NEUTRAL BACKDROP THAT ENHANCES THE FOCAL ELEMENTS. OVERLAID VERTICALLY ALONG THE LEFT SIDE OF THE IMAGE, THE WORD 'PAUL SOMENDRA IS REPEATED IN LARGE, BOLD BLACK LETTERS WITH A SLIGHT TRANSPARENCY EFFECT, CREATING A LAYERED, DYNAMIC LOOK INTERSPERSED WITHIN THIS TEXT ARE ICONIC DESIGN ELEMENTS: A PROMINENT NIKE LOGO IN RED NEAR THE TOP, A STYLIZED RED 'S' LOWER DOWN, AND A VERTICAL RED LINE THAT PUNCTUATES THE DESIGN. TO THE RIGHT, A RED GEOMETRIC FRAME SURROUNDS THE OBSCURED EYE, DRAWING ATTENTION TO THE INTERPLAY OF COLOUR AND FORM. AT THE BOTTOM RIGHT, THE PHRASE 'WORK SMART NOT HARD' IS WRITTEN IN BOLD RED CAPITAL LETTERS, WITH 'SMART' IN A SMALLER, ELEGANT CURSIVE SCRIPT BENEATH IT SIGNED OFF WITH 'GRAPHICS' IN A MATCHING STYLE, SUGGESTING A PERSONAL OR BRAND SIGNATURE. THE BOTTOM LEFT CORNER FEATURES THE HASHTAG #PAUL' IN RED. REINFORCING THE IDENTITY THEME. THE YOUNG MAN'S ATTIRE, A PARTIALLY VISIBLE BLACK LEATHER JACKET WITH AN OPEN COLLAR, ADDS A RUGGED YET STYLISH EDGE TO THE OVERALL AESTHETIC. THE LIGHTING IS SOFT YET DRAMATIC. HIGHLIGHTING THE TEXTURES OF HIS HAIR AND JACKET, WHILE THE RED ACCENTS POP VIVIDLY AGAINST THE GRAYSCALE TONES, CREATING A COHESIVE, HIGH-ENERGY VISUAL THAT BLENDS STREETWEAR CULTURE WITH GRAPHIC ARTISTRY. PHOTOREALISTIC, SHALLOW DEPTH OF FIELD, HIGH-RESOLUTION DSLR QUALITY, HASSELBLAD X2D 100C, SHALLOW DEPTH OF FIELD, SHARPLY FOCUSED ON ME. 4:5 ASPECT RATIO. MAKE IT 8K ULTRA REALISTIC, HYPER DETAILED",#0.5
                "turn this photo into a A highly stylized portrait of same person in image with sharp features ,flawless fair skin,wearing black t shirt ,black sunglasses and standing against a bold gradient background, confidently. The light is cinematic ,emphasizing his facial structure and giving a luxury fashion magazine vibe . Ultra realistic,high detail, editorial photography style. 4k resolution,symmetrical composition,minimal background elements.4:3 ratio"#0.5
            ]
        }
    
    def get_random_prompt(self, category: str) -> Optional[str]:
        """
        Get a random prompt from the specified category.
        
        Args:
            category (str): The category name to select from
            
        Returns:
            str: A randomly selected prompt from the category
            None: If category doesn't exist
        """
        if category not in self.prompts:
            return None
        
        return random.choice(self.prompts[category])
    
    def get_all_categories(self) -> List[str]:
        """
        Get all available categories.
        
        Returns:
            List[str]: List of all category names
        """
        return list(self.prompts.keys())
    
    def get_category_prompts(self, category: str) -> Optional[List[str]]:
        """
        Get all prompts from a specific category.
        
        Args:
            category (str): The category name
            
        Returns:
            List[str]: All prompts in the category
            None: If category doesn't exist
        """
        return self.prompts.get(category)
    
    def get_random_prompt_any_category(self) -> tuple:
        """
        Get a random prompt from any category.
        
        Returns:
            tuple: (category_name, prompt_text)
        """
        category = random.choice(list(self.prompts.keys()))
        prompt = random.choice(self.prompts[category])
        return category, prompt
    
    def add_custom_prompt(self, category: str, prompt: str) -> bool:
        """
        Add a custom prompt to an existing category.
        
        Args:
            category (str): The category to add to
            prompt (str): The prompt text to add
            
        Returns:
            bool: True if successful, False if category doesn't exist
        """
        if category not in self.prompts:
            return False
        
        self.prompts[category].append(prompt)
        return True
    
    def create_custom_category(self, category: str, prompts: List[str]) -> bool:
        """
        Create a new category with custom prompts.
        
        Args:
            category (str): The new category name
            prompts (List[str]): List of prompts for the category
            
        Returns:
            bool: True if successful, False if category already exists
        """
        if category in self.prompts:
            return False
        
        self.prompts[category] = prompts
        return True
