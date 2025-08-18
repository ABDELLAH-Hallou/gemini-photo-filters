class ImageFilterManager:
    def __init__(self):
        self.filters_prompts = {
            "brightness": "Globally adjust the **luminance values** to achieve optimal visual balance. {direction} the overall **brightness** by {amount} to {purpose}.",
            "contrast": "Precisely refine the image's **dynamic range** by manipulating the **contrast**. {direction} contrast by {amount} to {effect}.",
            "saturation": "Meticulously control the **vibrancy and intensity of colors** within the image. {direction} **saturation** by {amount} to {effect}.",
            "exposure": "Accurately calibrate the image's **overall light capture**. {direction} **exposure** by {amount} to {purpose}.",
            "shadows_highlights": "Intelligently recover and enhance detail in the image's **extreme tonal ranges**. {shadow_direction} **shadows** by {shadow_amount} and {highlight_direction} **highlights** by {highlight_amount} to {purpose}.",
            "sharpness": "Precisely define and enhance the **edge fidelity** within the image. {direction} **sharpness** by {amount} to {effect}.",
            "temperature_tint": "Artfully manipulate the image's **color cast and white balance**. Adjust **temperature** to {temperature_direction} ({temperature_color}) tones and **tint** to {tint_direction} ({tint_color}) hues to {effect}.",
            "vintage": "Evoke the timeless charm of **classic film photography**. Apply a subtle **desaturation** to mute colors, introduce a gentle **fade** to the shadows, and overlay a finely-grained **texture** to simulate film grain. Additionally, consider a slight **vignette** to focus attention and enhance the nostalgic feel.",
            "cinematic": "Craft a **stylized aesthetic** inspired by the silver screen. Start with a **color grading** that emphasizes specific hues (e.g., teal and orange), subtly **desaturate** the overall image, and apply a slight **anamorphic lens flare** effect. Adjust **contrast** for a dramatic look, and add a touch of **grain** for texture.",
            "black_white": "Transform the image into a **monochromatic masterpiece**. Carefully adjust the **contrast** to create a full tonal range, from deep blacks to bright whites. Experiment with different **filter simulations** (e.g., red, green, blue) to alter the tonal interpretation of colors. Aim for a balanced and impactful **grayscale** representation.",
            "portrait": "Enhance the **subject's natural beauty** and create a flattering **portrait**. Gently **soften skin textures** while maintaining sharpness in the eyes and other key features. Warm up **skin tones** for a healthy glow, and subtly **blur the background** to isolate the subject and minimize distractions.",
            "mood_based": "Infuse the image with a **{mood}** emotional atmosphere by {intensity}. {adjustments}",#
            "instagram_presets": "Emulate the **{preset_name}** filter style found on social media. Apply the characteristic {characteristics} to achieve the {preset_name} aesthetic.",
            "curves": "Precisely manipulate the **tonal range** of the image by adjusting the **Curves**. Apply a **{curve_type}** curve adjustment by {intensity} to {effect}.",#
            
            "split_toning": "Precisely apply a split toning effect to create a harmonious color contrast. Infuse the shadows with a {shadow_color} hue at a saturation level of {shadow_saturation}%, and simultaneously introduce a {highlight_color} hue into the highlights at a saturation level of {highlight_saturation}%. This combination should achieve a {desired_look} aesthetic.",    
            
            "hsl": """Precisely adjust the hue, saturation, and lightness of {target_colors} within the image.

Hue Shift: Apply a hue shift of {hue_shift} degrees to subtly or drastically alter the selected colors. Positive values shift the hue clockwise on the color wheel, while negative values shift it counter-clockwise.
Saturation Change: Modify the vibrancy of the selected colors by {saturation_change}%. Positive values increase color intensity, while negative values reduce it, potentially leading towards grayscale.
Lightness Change: Adjust the brightness of the selected colors by {lightness_change}%. Positive values brighten the colors, while negative values darken them.
These adjustments should {adjustments} to achieve the desired color balance and visual effect.""",
            "crop_rotate": """Precisely refine the image's composition and orientation for optimal visual impact.

Cropping: {crop_instruction}.
If selecting 'Custom crop', set the dimensions to {custom_width} pixels wide by {custom_height} pixels high.

Rotation: {rotate_instruction}.
If selecting 'Custom angle', rotate the image by {rotate_angle} degrees (clockwise for positive values, counter-clockwise for negative values).

These adjustments aim to improve framing, correct any tilting, and ensure a balanced, aesthetically pleasing result.""",
            "flip_mirror": "Create a **symmetrical reflection** of the image. **Flip** the image {direction} to {effect}.",
            "vignette": "Introduce a {intensity} **{vignette_type} vignette** effect around the edges of the image. Control the **shape, size, and feathering** to {effect}.",
            "grain_noise": "Simulate the **texture and character of film** by adding **{grain_type}** {effect_type}. Apply {intensity} intensity to achieve a {aesthetic} aesthetic.",
            "blur": "Soften or stylize the image using **{blur_type}** blur effect. Apply {intensity} blur with {direction_info} to {effect}.",
            "light_leaks_flares": "Emulate the artistic imperfections of analog photography by adding {effect_type}. Create {color} {effect_description} with an intensity of {intensity} strength, positioned at the {placement} of the image. If 'custom' color is selected, use hex color {custom_color}.",
            "glitch_pixelate_sketch": "Create **stylized {effect_type}** distortions with {intensity} intensity to achieve a {aesthetic} aesthetic.",
            "auto_enhance": "Initiate an **intelligent, AI-driven optimization** of the image. Apply an **auto-enhance** function to globally adjust **brightness, contrast, saturation, and white balance** for optimal visual appeal. Prioritize a natural-looking result that corrects common imperfections without over-processing.",
            "sky_replacement": """Leverage advanced AI to detect and seamlessly replace the sky in the image. Integrate a {sky_type} sky.

If '{sky_type}' is set to 'custom', describe the desired sky as: {custom_sky_type}.

Ensure the new sky integrates naturally with the existing scene's lighting, perspective, and color temperature for a realistic and harmonious result.""",
            "background_removal_blur": "Precisely **isolate the primary subject** from its surroundings. {action} to {effect}.",
            "face_retouch": "Subtly enhance facial features for a refined and natural look. Apply **skin smoothing** to reduce imperfections while retaining natural texture, **whiten teeth**, and **brighten/sharpen eyes** to add sparkle. Ensure all adjustments are gentle and maintain the subject's authentic appearance.",
            "object_removal": """Intelligently identify and seamlessly remove {objects} from the image.

If '{objects}' is set to 'custom objects', specifically target: {custom_objects}.

Ensure the void is filled with surrounding textures and patterns, resulting in a clean and undetectable repair.""",
            "style_transfer": "Apply the **artistic aesthetic** of a **{style_reference}** to the target photograph. Imbue the photo with the unique {style_characteristics} while preserving the photo's original content.",
            "add_text": """Integrate the text '{text_content}' onto the image.

Font & Style: Use a {font_style} font, set to {font_size}px for optimal readability.
Color: Apply a {color} color. If 'custom color' is selected, use {custom_color}.
Placement: Position the text at {x_position}% horizontally and {y_position}% vertically on the image.
Orientation & Visibility: Rotate the text by {rotation} degrees and set its opacity to {opacity} alpha.
Alignment & Background: Align the text to the {alignment}. {background_option} behind the text for enhanced visibility and style.""",
            "stickers_emojis": "Incorporate {element_type} onto the image. Specify the {element_description} you want to add. Place the element at {x_position}% horizontally and {y_position}% vertically. Set its size to {size}px, rotate it by {rotation} degrees, and adjust its transparency to {opacity} alpha.",
            "brush_draw": """Utilize a {brush_type} digital brush for {purpose} on the image.

Brush Properties: Use a {color} color (if 'custom color' is selected, use {custom_color}), set the brush size to {brush_size}px, and adjust the opacity to {opacity} alpha.

Drawing Action: Perform the following drawing action: {drawing_instructions}.""",
            "frames_borders": """Encase the image with a {frame_style} frame or border to achieve a {effect}.

Frame Appearance:

Thickness: Set the thickness to {thickness}px.
Color: Apply a {color} color (if 'custom color' is selected, use {custom_color}).
Texture: Choose a {texture} texture for the border.
Corner Radius: Apply a corner radius of {corner_radius}px for rounded corners (0 for sharp corners)."""
        }
        self.filter_parameters = {
            "brightness": {
                "direction": ["Increase", "Decrease"],
                "amount": {"type": "slider", "min": 0.1, "max": 2.0, "default": 1.0, "step": 0.1, "unit": "multiplier"},
                "purpose": ["reveal hidden details in shadows", "enhance mood and create dramatic effect", "balance exposure", "correct underexposure"]
            },
            "contrast": {
                "direction": ["Increase", "Decrease"],
                "amount": {"type": "slider", "min": 0.5, "max": 3.0, "default": 1.0, "step": 0.1, "unit": "multiplier"},
                "effect": ["deepen blacks and brighten whites", "create softer ethereal aesthetic", "enhance visual impact", "improve definition"]
            },
            "saturation": {
                "direction": ["Increase", "Decrease"],
                "amount": {"type": "slider", "min": 0.0, "max": 2.0, "default": 1.0, "step": 0.1, "unit": "multiplier"},
                "effect": ["make colors pop and appear vivid", "create muted vintage appearance", "achieve monochromatic look", "enhance color vibrancy"]
            },
            "exposure": {
                "direction": ["Increase", "Decrease"],
                "amount": {"type": "slider", "min": -2.0, "max": 2.0, "default": 0.0, "step": 0.1, "unit": "stops"},
                "purpose": ["brighten underexposed areas", "correct overexposed highlights", "balance overall exposure", "enhance tonal richness"]
            },
            "shadows_highlights": {
                "shadow_direction": ["Lighten", "Darken"],
                "shadow_amount": {"type": "slider", "min": 0, "max": 100, "default": 0, "step": 1, "unit": "%"},
                "highlight_direction": ["Brighten", "Darken"],
                "highlight_amount": {"type": "slider", "min": 0, "max": 100, "default": 0, "step": 1, "unit": "%"},
                "purpose": ["balance exposure", "recover lost details", "enhance dynamic range", "create dramatic effect"]
            },
            "sharpness": {
                "direction": ["Increase", "Decrease"],
                "amount": {"type": "slider", "min": 0.0, "max": 3.0, "default": 1.0, "step": 0.1, "unit": "multiplier"},
                "effect": ["enhance textural details", "create crisp appearance", "soften harsh edges", "improve clarity"]
            },
            "temperature_tint": {
                "temperature_direction": ["warmer", "cooler"],
                "temperature_color": ["yellow/orange", "blue"],
                "tint_direction": ["add green", "add magenta", "neutralize"],
                "effect": ["golden hour feel", "serene cinematic mood", "neutralize color casts", "artistic color grading"]
            },
            "mood_based": {
                "mood": ["warm", "cool", "dramatic", "romantic", "vintage", "modern", "ethereal", "melancholic"],
                "intensity": {"type": "slider", "min": 0.1, "max": 2.0, "default": 1.0, "step": 0.1, "unit": "multiplier"},
                "adjustments": ["increase temperature and add golden hues", "lower temperature and emphasize blues", "increase contrast and darken shadows", "add soft pink tones and reduce contrast", "enhance earth tones", "create high-key bright look"]
            },
            "instagram_presets": {
                "preset_name": ["Clarendon", "Juno", "Lark", "Ludwig", "Valencia", "X-Pro II", "Willow", "Rise", "Hudson"],
                "characteristics": ["high contrast and bright colors", "soft warm tones", "desaturated with green tint", "vintage with faded edges", "warm yellow tint", "dramatic vignette and color shift", "black and white with silver tones", "golden warm glow", "cool tones with border"]
            },
            "curves": {
                "curve_type": ["S-curve", "lifted shadows", "crushed blacks", "faded film", "custom"],
                "intensity": {"type": "slider", "min": 0.1, "max": 2.0, "default": 1.0, "step": 0.1, "unit": "strength"},
                "effect": ["increase contrast", "brighten dark areas", "create vintage look", "enhance highlights", "fine-tune specific tones"]
            },
            "split_toning": {
                "shadow_color": ["black","blue", "teal", "purple", "orange", "green", "magenta"],
                "shadow_saturation": {"type": "slider", "min": 0, "max": 100, "default": 25, "step": 1, "unit": "%"},
                "highlight_color": ["orange", "yellow", "pink", "cyan", "warm white", "cool white"],
                "highlight_saturation": {"type": "slider", "min": 0, "max": 100, "default": 25, "step": 1, "unit": "%"},
                "desired_look": ["cinematic", "vintage", "modern", "artistic", "natural"]
            },
            "hsl": {
                "target_colors": ["all colors", "reds", "oranges", "yellows", "greens", "cyans", "blues", "purples", "magentas"],
                "hue_shift": {"type": "slider", "min": -180, "max": 180, "default": 0, "step": 1, "unit": "degrees"},
                "saturation_change": {"type": "slider", "min": -100, "max": 100, "default": 0, "step": 1, "unit": "%"},
                "lightness_change": {"type": "slider", "min": -100, "max": 100, "default": 0, "step": 1, "unit": "%"},
                "adjustments": ["shift hue slightly", "increase saturation", "decrease saturation", "brighten", "darken", "fine-tune color balance"]
            },
            "crop_rotate": {
                "crop_instruction": ["Crop to 16:9 aspect ratio", "Crop to square format", "Crop to 4:3 ratio", "Remove unwanted edges", "Focus on main subject", "Custom crop"],
                "custom_width": {"type": "number_input", "min": 100, "max": 8000, "default": 1920, "unit": "pixels"},
                "custom_height": {"type": "number_input", "min": 100, "max": 8000, "default": 1080, "unit": "pixels"},
                "rotate_angle": {"type": "slider", "min": -180, "max": 180, "default": 0, "step": 1, "unit": "degrees"},
                "rotate_instruction": ["Rotate 90° clockwise", "Rotate 90° counter-clockwise", "Straighten horizon", "Correct perspective", "Custom angle"]
            },
            "flip_mirror": {
                "direction": ["horizontally", "vertically", "both"],
                "effect": ["mirror left and right sides", "invert top and bottom", "create symmetrical composition", "correct perspective"]
            },
            "vignette": {
                "intensity": {"type": "slider", "min": 0.0, "max": 1.0, "default": 0.3, "step": 0.05, "unit": "strength"},
                "vignette_type": ["dark", "light"],
                "effect": ["focus attention on center", "add depth and mood", "create soft ethereal quality", "enhance artistic composition"]
            },
            "grain_noise": {
                "grain_type": ["fine", "coarse", "film"],
                "effect_type": ["grain", "noise"],
                "intensity": {"type": "slider", "min": 0.0, "max": 1.0, "default": 0.2, "step": 0.05, "unit": "strength"},
                "aesthetic": ["vintage", "gritty", "cinematic", "artistic"]
            },
            "blur": {
                "blur_type": ["Gaussian", "motion", "lens", "radial"],
                "intensity": {"type": "slider", "min": 0.1, "max": 2.0, "default": 1.0, "step": 0.1, "unit": "strength"},
                "direction_info": ["no specific direction", "horizontal motion", "vertical motion", "radial from center"],
                "effect": ["smooth overall softening", "simulate movement", "create shallow depth of field", "artistic stylization"]
            },
            "light_leaks_flares": {
                "effect_type": ["light leaks", "lens flares"],
                "color": ["warm orange", "bright white", "colorful rainbow", "soft pink", "golden yellow", "custom"],
                "custom_color": {"type": "text_input", "default": "#FF6B35", "placeholder": "Enter hex color (e.g., #FF6B35)"},
                "intensity": {"type": "slider", "min": 0.1, "max": 1.0, "default": 0.5, "step": 0.05, "unit": "strength"},
                "effect_description": ["streaks of light", "circular flares", "washing light effects", "vintage light leaks"],
                "placement": ["top corner", "bottom corner", "center", "edge", "custom position"]
            },
            "glitch_pixelate_sketch": {
                "effect_type": ["glitch", "pixelate", "sketch"],
                "intensity": {"type": "slider", "min": 0.1, "max": 1.0, "default": 0.5, "step": 0.05, "unit": "strength"},
                "aesthetic": ["modern edgy", "retro digital", "artistic stylized", "abstract"]
            },
            "sky_replacement": {
                "sky_type": ["dramatic sunset", "clear blue", "stormy clouds", "starry night", "golden hour", "overcast", "rainbow", "twilight purple", "custom"],
                "custom_sky_type": {"type": "text_input", "default": "", "placeholder": "Describe the sky you want (e.g., pink cotton candy clouds)"}
            },
            "background_removal_blur": {
                "action": ["Completely remove the background", "Apply strong background blur", "Apply subtle background blur"],
                "effect": ["create transparent image for compositing", "achieve professional bokeh effect", "isolate subject naturally"]
            },
            "object_removal": {
                "objects": ["unwanted people", "power lines", "trash/litter", "vehicles", "signs", "blemishes", "custom objects"],
                "custom_objects": {"type": "text_input", "default": "", "placeholder": "Describe objects to remove (e.g., red car, street lamp)"}
            },
            "style_transfer": {
                "style_reference": ["Impressionist painting", "Van Gogh style", "Pencil sketch", "Pop art", "Watercolor", "Oil painting", "Comic book style", "Custom style"],
                "custom_style_reference": {"type": "text_input", "default": "", "placeholder": "Describe the artistic style you want"},
                "style_characteristics": ["brushstrokes and color palette", "swirling textures and vibrant colors", "pencil lines and shading", "bold colors and high contrast", "soft washes and bleeding", "thick paint texture", "bold outlines and flat colors"]
            },
            "add_text": {
                "text_content": {"type": "text_input", "default": "", "placeholder": "Enter your text here"},
                "font_style": ["modern sans-serif", "classic serif", "handwritten", "bold impact", "elegant script"],
                "font_size": {"type": "slider", "min": 8, "max": 200, "default": 24, "step": 2, "unit": "px"},
                "color": ["white", "black", "red", "blue", "yellow", "custom color"],
                "custom_color": {"type": "text_input", "default": "#FFFFFF", "placeholder": "Enter hex color (e.g., #FFFFFF)"},
                "x_position": {"type": "slider", "min": 0, "max": 100, "default": 50, "step": 1, "unit": "%"},
                "y_position": {"type": "slider", "min": 0, "max": 100, "default": 50, "step": 1, "unit": "%"},
                "rotation": {"type": "slider", "min": -45, "max": 45, "default": 0, "step": 1, "unit": "degrees"},
                "opacity": {"type": "slider", "min": 0.1, "max": 1.0, "default": 1.0, "step": 0.05, "unit": "alpha"},
                "alignment": ["left", "center", "right"],
                "background_option": ["No background", "Add semi-transparent background", "Add solid background", "Add outline"]
            },
            "stickers_emojis": {
                "element_type": ["decorative stickers", "emojis", "icons", "badges"],
                "element_description": {"type": "text_input", "default": "", "placeholder": "Describe stickers/emojis (e.g., heart symbols, star decorations)"},
                "x_position": {"type": "slider", "min": 0, "max": 100, "default": 50, "step": 1, "unit": "%"},
                "y_position": {"type": "slider", "min": 0, "max": 100, "default": 50, "step": 1, "unit": "%"},
                "size": {"type": "slider", "min": 10, "max": 200, "default": 50, "step": 5, "unit": "px"},
                "rotation": {"type": "slider", "min": 0, "max": 360, "default": 0, "step": 15, "unit": "degrees"},
                "opacity": {"type": "slider", "min": 0.1, "max": 1.0, "default": 1.0, "step": 0.05, "unit": "alpha"}
            },
            "brush_draw": {
                "brush_type": ["solid", "textured", "feathered", "calligraphy"],
                "purpose": ["freehand drawing", "precise annotations", "artistic embellishments", "highlighting areas"],
                "color": ["red", "blue", "yellow", "white", "black", "custom color"],
                "custom_color": {"type": "text_input", "default": "#FF0000", "placeholder": "Enter hex color (e.g., #FF0000)"},
                "brush_size": {"type": "slider", "min": 1, "max": 50, "default": 5, "step": 1, "unit": "px"},
                "opacity": {"type": "slider", "min": 0.1, "max": 1.0, "default": 1.0, "step": 0.05, "unit": "alpha"},
                "drawing_instructions": {"type": "text_input", "default": "", "placeholder": "Describe what to draw (e.g., circle around face, arrow pointing to...)"}
            },
            "frames_borders": {
                "frame_style": ["simple line", "ornate decorative", "vintage", "modern minimalist", "polaroid style"],
                "thickness": {"type": "slider", "min": 1, "max": 50, "default": 5, "step": 1, "unit": "px"},
                "color": ["white", "black", "gold", "silver", "custom color"],
                "custom_color": {"type": "text_input", "default": "#FFFFFF", "placeholder": "Enter hex color (e.g., #FFFFFF)"},
                "corner_radius": {"type": "slider", "min": 0, "max": 50, "default": 0, "step": 1, "unit": "px"},
                "texture": ["solid", "textured", "gradient", "patterned"],
                "effect": ["subtle separation", "elegant presentation", "vintage feel", "modern accent"]
            }
        }
        self.basic_filters = ['brightness', 'contrast', 'saturation', 'exposure', 'sharpness']
        self.color_filters = ['temperature_tint', 'hsl', 'split_toning', 'curves']
        self.artistic_filters = ['vintage', 'cinematic', 'black_white', 'mood_based', 'instagram_presets']
        self.effects_filters = ['vignette', 'grain_noise', 'blur', 'light_leaks_flares', 'glitch_pixelate_sketch']
        self.ai_filters = ['auto_enhance', 'sky_replacement', 'background_removal_blur', 'face_retouch', 'object_removal', 'style_transfer']
        self.editing_filters = ['crop_rotate', 'flip_mirror']
        self.overlay_filters = ['add_text', 'stickers_emojis', 'brush_draw', 'frames_borders']

        self.filter_categories = {
            "📊 Basic Adjustments": self.basic_filters,
            "🎨 Color & Tone": self.color_filters,
            "🎭 Artistic Styles": self.artistic_filters,
            "✨ Visual Effects": self.effects_filters,
            "🤖 AI-Powered": self.ai_filters,
            "📐 Transform & Edit": self.editing_filters,
            "📝 Overlays & Text": self.overlay_filters
        }
    def format_filter_prompt(self, filter_name, **kwargs):
        if filter_name not in self.filters_prompts:
            raise ValueError(f"Filter '{filter_name}' not found in filters_prompts")
        
        return self.filters_prompts[filter_name].format(**kwargs)

    def get_filter_categories(self):
        return self.filter_categories
    
    def get_all_prompts(self):
        return self.filters_prompts
    
    def get_filter_prompt(self,filter):
        if filter not in self.filters_prompts.keys():
            raise KeyError("Filter does not exists in the bank of filters")
        return self.filters_prompts[filter]
    
    def get_all_parameters(self):
        return self.filter_parameters
    
    def get_filter_parameters(self,filter):
        if filter not in self.filter_parameters.keys():
            raise KeyError("Filter does not have parametrs")
        return self.filter_parameters[filter]
    
    def combine_filter_prompts(self, configured_filters):
        if not configured_filters:
            return ""
        
        combined_prompts = []
        
        for filter_name, params in configured_filters.items():
            try:
                if params:  
                    formatted_prompt = self.format_filter_prompt(filter_name, **params)
                else:  
                    formatted_prompt = self.filters_prompts[filter_name]
                
                combined_prompts.append(f"**{filter_name.replace('_', ' ').title()}:** {formatted_prompt}")
            except KeyError as e:
                continue
        
        if combined_prompts:
            final_prompt = "Apply the following image processing filters and adjustments:\n\n" + "\n\n".join(combined_prompts)
            final_prompt += "\n\nEnsure all adjustments work harmoniously together to create a cohesive and visually appealing result. Maintain the natural look of the image while applying the specified enhancements."
            return final_prompt
        
        return ""