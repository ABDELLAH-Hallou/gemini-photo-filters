filters_prompts = {
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
def format_filter_prompt(filter_name, **kwargs):
    """Format a filter prompt with user-provided parameters."""
    if filter_name not in filters_prompts:
        raise ValueError(f"Filter '{filter_name}' not found in filters_prompts")
    
    return filters_prompts[filter_name].format(**kwargs)

basic_filters = ['brightness', 'contrast', 'saturation', 'exposure', 'sharpness']
color_filters = ['temperature_tint', 'hsl', 'split_toning', 'curves']
artistic_filters = ['vintage', 'cinematic', 'black_white', 'mood_based', 'instagram_presets']
effects_filters = ['vignette', 'grain_noise', 'blur', 'light_leaks_flares', 'glitch_pixelate_sketch']
ai_filters = ['auto_enhance', 'sky_replacement', 'background_removal_blur', 'face_retouch', 'object_removal', 'style_transfer']
editing_filters = ['crop_rotate', 'flip_mirror']
overlay_filters = ['add_text', 'stickers_emojis', 'brush_draw', 'frames_borders']

filter_categories = {
    "📊 Basic Adjustments": basic_filters,
    "🎨 Color & Tone": color_filters,
    "🎭 Artistic Styles": artistic_filters,
    "✨ Visual Effects": effects_filters,
    "🤖 AI-Powered": ai_filters,
    "📐 Transform & Edit": editing_filters,
    "📝 Overlays & Text": overlay_filters
}