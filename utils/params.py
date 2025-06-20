# filter_parameters = {
#     "brightness": {
#         "direction": ["Increase", "Decrease"],
#         "amount": ["slightly", "moderately", "significantly", "dramatically"],
#         "purpose": ["reveal hidden details in shadows", "enhance mood and create dramatic effect", "balance exposure", "correct underexposure"]
#     },
#     "contrast": {
#         "direction": ["Increase", "Decrease"],
#         "amount": ["slightly", "moderately", "significantly"],
#         "effect": ["deepen blacks and brighten whites", "create softer ethereal aesthetic", "enhance visual impact", "improve definition"]
#     },
#     "saturation": {
#         "direction": ["Increase", "Decrease"],
#         "amount": ["slightly", "moderately", "significantly"],
#         "effect": ["make colors pop and appear vivid", "create muted vintage appearance", "achieve monochromatic look", "enhance color vibrancy"]
#     },
#     "exposure": {
#         "direction": ["Increase", "Decrease"],
#         "amount": ["slightly", "moderately", "significantly"],
#         "purpose": ["brighten underexposed areas", "correct overexposed highlights", "balance overall exposure", "enhance tonal richness"]
#     },
#     "shadows_highlights": {
#         "shadow_direction": ["Lighten", "Darken"],
#         "shadow_amount": ["slightly", "moderately", "significantly"],
#         "highlight_direction": ["Brighten", "Darken"],
#         "highlight_amount": ["slightly", "moderately", "significantly"],
#         "purpose": ["balance exposure", "recover lost details", "enhance dynamic range", "create dramatic effect"]
#     },
#     "sharpness": {
#         "direction": ["Increase", "Decrease"],
#         "amount": ["slightly", "moderately", "significantly"],
#         "effect": ["enhance textural details", "create crisp appearance", "soften harsh edges", "improve clarity"]
#     },
#     "temperature_tint": {
#         "temperature_direction": ["warmer", "cooler"],
#         "temperature_color": ["yellow/orange", "blue"],
#         "tint_direction": ["add green", "add magenta", "neutralize"],
#         "tint_color": ["green", "magenta", "balanced"],
#         "effect": ["golden hour feel", "serene cinematic mood", "neutralize color casts", "artistic color grading"]
#     },
#     "mood_based": {
#         "mood": ["warm", "cool", "dramatic", "romantic", "vintage", "modern", "ethereal", "melancholic"],
#         "adjustments": ["increase temperature and add golden hues", "lower temperature and emphasize blues", "increase contrast and darken shadows", "add soft pink tones and reduce contrast", "enhance earth tones", "create high-key bright look"]
#     },
#     "instagram_presets": {
#         "preset_name": ["Clarendon", "Juno", "Lark", "Ludwig", "Valencia", "X-Pro II", "Willow", "Rise", "Hudson"],
#         "characteristics": ["high contrast and bright colors", "soft warm tones", "desaturated with green tint", "vintage with faded edges", "warm yellow tint", "dramatic vignette and color shift", "black and white with silver tones", "golden warm glow", "cool tones with border"]
#     },
#     "curves": {
#         "curve_type": ["S-curve", "lifted shadows", "crushed blacks", "faded film", "custom"],
#         "effect": ["increase contrast", "brighten dark areas", "create vintage look", "enhance highlights", "fine-tune specific tones"]
#     },
#     "split_toning": {
#         "shadow_color": ["blue", "teal", "purple", "orange", "green", "magenta"],
#         "highlight_color": ["orange", "yellow", "pink", "cyan", "warm white", "cool white"],
#         "saturation_level": ["low", "medium", "high"],
#         "desired_look": ["cinematic", "vintage", "modern", "artistic", "natural"]
#     },
#     "hsl": {
#         "target_colors": ["all colors", "reds", "oranges", "yellows", "greens", "cyans", "blues", "purples", "magentas"],
#         "adjustments": ["shift hue slightly", "increase saturation", "decrease saturation", "brighten", "darken", "fine-tune color balance"]
#     },
#     "crop_rotate": {
#         "crop_instruction": ["Crop to 16:9 aspect ratio", "Crop to square format", "Crop to 4:3 ratio", "Remove unwanted edges", "Focus on main subject"],
#         "rotate_instruction": ["Rotate 90° clockwise", "Rotate 90° counter-clockwise", "Straighten horizon", "Correct perspective", "No rotation needed"]
#     },
#     "flip_mirror": {
#         "direction": ["horizontally", "vertically"],
#         "effect": ["mirror left and right sides", "invert top and bottom", "create symmetrical composition", "correct perspective"]
#     },
#     "resize": {
#         "target_size": ["1920x1080 pixels", "1080x1080 pixels", "3840x2160 pixels", "50% of original", "200% of original", "custom dimensions"],
#         "method_instruction": ["Maintain aspect ratio", "Stretch to fit", "Use bicubic resampling", "Optimize for web", "Preserve quality"]
#     },
#     "vignette": {
#         "intensity": ["subtle", "moderate", "dramatic"],
#         "vignette_type": ["dark", "light"],
#         "effect": ["focus attention on center", "add depth and mood", "create soft ethereal quality", "enhance artistic composition"]
#     },
#     "grain_noise": {
#         "grain_type": ["fine", "coarse", "film"],
#         "effect_type": ["grain", "noise"],
#         "intensity": ["low", "medium", "high"],
#         "aesthetic": ["vintage", "gritty", "cinematic", "artistic"]
#     },
#     "blur": {
#         "blur_type": ["Gaussian", "motion", "lens", "radial"],
#         "intensity": ["light", "moderate", "heavy"],
#         "direction_info": ["no specific direction", "horizontal motion", "vertical motion", "radial from center"],
#         "effect": ["smooth overall softening", "simulate movement", "create shallow depth of field", "artistic stylization"]
#     },
#     "light_leaks_flares": {
#         "effect_type": ["light leaks", "lens flares"],
#         "color": ["warm orange", "bright white", "colorful rainbow", "soft pink", "golden yellow"],
#         "effect_description": ["streaks of light", "circular flares", "washing light effects", "vintage light leaks"],
#         "intensity": ["subtle", "moderate", "dramatic"],
#         "placement": ["top corner", "bottom corner", "center", "edge", "multiple positions"]
#     },
#     "glitch_pixelate_sketch": {
#         "effect_type": ["glitch", "pixelate", "sketch"],
#         "intensity": ["low", "medium", "high"],
#         "aesthetic": ["modern edgy", "retro digital", "artistic stylized", "abstract"]
#     },
#     "sky_replacement": {
#         "sky_type": ["dramatic sunset", "clear blue", "stormy clouds", "starry night", "golden hour", "overcast", "rainbow", "twilight purple"]
#     },
#     "background_removal_blur": {
#         "action": ["Completely remove the background", "Apply strong background blur", "Apply subtle background blur"],
#         "effect": ["create transparent image for compositing", "achieve professional bokeh effect", "isolate subject naturally"]
#     },
#     "object_removal": {
#         "objects": ["unwanted people", "power lines", "trash/litter", "vehicles", "signs", "specific objects", "blemishes"]
#     },
#     "style_transfer": {
#         "style_reference": ["Impressionist painting", "Van Gogh style", "Pencil sketch", "Pop art", "Watercolor", "Oil painting", "Comic book style"],
#         "style_characteristics": ["brushstrokes and color palette", "swirling textures and vibrant colors", "pencil lines and shading", "bold colors and high contrast", "soft washes and bleeding", "thick paint texture", "bold outlines and flat colors"]
#     },
#     "add_text": {
#         "text_content": ["Custom text", "Watermark", "Title", "Caption", "Logo text"],
#         "font_style": ["modern sans-serif", "classic serif", "handwritten", "bold impact", "elegant script"],
#         "size": ["small", "medium", "large", "extra large"],
#         "color": ["white", "black", "red", "blue", "yellow", "custom color"],
#         "alignment": ["left", "center", "right"],
#         "background_option": ["No background", "Add semi-transparent background", "Add solid background", "Add outline"]
#     },
#     "stickers_emojis": {
#         "element_type": ["decorative stickers", "emojis", "icons", "badges"],
#         "element_description": ["heart symbols", "star decorations", "nature elements", "geometric shapes"],
#         "placement": ["top left", "top right", "bottom left", "bottom right", "center", "custom position"],
#         "size": ["small", "medium", "large"],
#         "rotation": ["0°", "45°", "90°", "random"],
#         "opacity": ["25%", "50%", "75%", "100%"]
#     },
#     "brush_draw": {
#         "brush_type": ["solid", "textured", "feathered", "calligraphy"],
#         "purpose": ["freehand drawing", "precise annotations", "artistic embellishments", "highlighting areas"],
#         "color": ["red", "blue", "yellow", "white", "black", "custom color"],
#         "size": ["thin", "medium", "thick", "variable"],
#         "opacity": ["25%", "50%", "75%", "100%"],
#         "effect": ["bold statements", "subtle annotations", "artistic touches", "technical markup"]
#     },
#     "frames_borders": {
#         "frame_style": ["simple line", "ornate decorative", "vintage", "modern minimalist", "polaroid style"],
#         "thickness": ["thin", "medium", "thick"],
#         "color": ["white", "black", "gold", "silver", "custom color"],
#         "texture": ["solid", "textured", "gradient", "patterned"],
#         "effect": ["subtle separation", "elegant presentation", "vintage feel", "modern accent"]
#     }
# }
filter_parameters = {
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