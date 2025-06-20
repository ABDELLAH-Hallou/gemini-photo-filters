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
    "mood_based": "Infuse the image with a **{mood}** emotional atmosphere. {adjustments}",
    "instagram_presets": "Emulate the **{preset_name}** filter style found on social media. Apply the characteristic {characteristics} to achieve the {preset_name} aesthetic.",
    "curves": "Precisely manipulate the **tonal range** of the image by adjusting the **Curves**. Apply a **{curve_type}** curve adjustment to {effect}.",
    "split_toning": "Introduce a **harmonious color contrast** by applying {shadow_color} hues to the **shadows** and {highlight_color} hues to the **highlights**. Balance the saturation at {saturation_level} to achieve a {desired_look} look.",
    "hsl": "Individually fine-tune the **hue, saturation, and lightness** of {target_colors} within the image. {adjustments}",
    "crop_rotate": "Precisely refine the image's **composition and orientation**. {crop_instruction} {rotate_instruction}",
    "flip_mirror": "Create a **symmetrical reflection** of the image. **Flip** the image {direction} to {effect}.",
    "perspective_skew": "Correct or creatively manipulate the image's **apparent viewpoint**. Adjust the **perspective** to fix converging lines in architectural photos, or intentionally **skew** the image to create a dynamic or distorted effect. This allows for precise control over the image's geometry and spatial relationships.",
    "resize": "Change the image's **physical dimensions** to {target_size}. {method_instruction}",
    "vignette": "Introduce a {intensity} **{vignette_type} vignette** effect around the edges of the image. Control the **shape, size, and feathering** to {effect}.",
    "grain_noise": "Simulate the **texture and character of film** by adding **{grain_type}** {effect_type}. Apply {intensity} intensity to achieve a {aesthetic} aesthetic.",
    "blur": "Soften or stylize the image using **{blur_type}** blur effect. Apply {intensity} blur with {direction_info} to {effect}.",
    "light_leaks_flares": "Emulate the **artistic imperfections** of analog photography by adding **{effect_type}**. Create {color} {effect_description} with {intensity} intensity positioned at {placement}.",
    "glitch_pixelate_sketch": "Create **stylized {effect_type}** distortions with {intensity} intensity to achieve a {aesthetic} aesthetic.",
    "auto_enhance": "Initiate an **intelligent, AI-driven optimization** of the image. Apply an **auto-enhance** function to globally adjust **brightness, contrast, saturation, and white balance** for optimal visual appeal. Prioritize a natural-looking result that corrects common imperfections without over-processing.",
    "sky_replacement": "Leverage advanced AI to **detect and seamlessly replace the sky** with a **{sky_type}** sky. Ensure the new sky **integrates naturally** with the existing scene's lighting, perspective, and color temperature.",
    "background_removal_blur": "Precisely **isolate the primary subject** from its surroundings. {action} to {effect}.",
    "face_retouch": "Subtly enhance facial features for a refined and natural look. Apply **skin smoothing** to reduce imperfections while retaining natural texture, **whiten teeth**, and **brighten/sharpen eyes** to add sparkle. Ensure all adjustments are gentle and maintain the subject's authentic appearance.",
    "object_removal": "Intelligently **identify and seamlessly remove** {objects} from the image. Fill the void with surrounding textures and patterns, ensuring a clean and undetectable repair.",
    "style_transfer": "Apply the **artistic aesthetic** of a **{style_reference}** to the target photograph. Imbue the photo with the unique {style_characteristics} while preserving the photo's original content.",
    "add_text": "Integrate **{text_content}** onto the image using **{font_style}** font. Set the size to {size} for optimal readability, use {color} color, and position it with {alignment} alignment. {background_option}",
    "stickers_emojis": "Incorporate **{element_type}** onto the image. Position {element_description} at {placement} with {size} size, {rotation} rotation, and {opacity} opacity.",
    "brush_draw": "Utilize a **{brush_type}** digital brush for {purpose} on the image. Use {color} color with {size} size and {opacity} opacity for {effect}.",
    "frames_borders": "Encase the image with a **{frame_style}** frame/border. Apply {thickness} thickness using {color} color and {texture} texture to {effect}."
}
def format_filter_prompt(filter_name, **kwargs):
    """Format a filter prompt with user-provided parameters."""
    if filter_name not in filters_prompts:
        raise ValueError(f"Filter '{filter_name}' not found in filters_prompts")
    
    return filters_prompts[filter_name].format(**kwargs)