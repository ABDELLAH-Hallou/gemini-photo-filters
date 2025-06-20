from typing import Dict
def get_category_display_names() -> Dict[str, str]:
    """
    display names for categories for Streamlit dropdown menus.
    
    Returns:
        Dict[str, str]: Mapping of internal names to display names
    """
    return {
        "quality_enhancement": "Quality Enhancement",
        "artistic_style": "Artistic Style",
        "mood_atmosphere": "Mood & Atmosphere",
        "portrait_enhancement": "Portrait Enhancement",
        "landscape_nature": "Landscape & Nature",
        "creative_artistic": "Creative & Artistic"
    }

