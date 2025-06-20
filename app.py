import streamlit as st
import os
import tempfile
import zipfile
from pathlib import Path
from datetime import datetime
from typing import List, Optional
import time
import yaml
from engine import (
    GeminiEnhancementEngine,
    ImageConfig,
    GeminiConfig
)
from utils.about import ABOUT
from utils.helper import get_category_display_names
from utils.image import (
    ImageConfig
)
from prompts import (
    PhotoPromptSelector
)
def load_config(path="data.yaml"):
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)
CONFIG = load_config()
st.set_page_config(
    page_title=CONFIG["app"]["page_title"],
    page_icon=CONFIG["app"]["page_icon"],
    layout="wide",
    initial_sidebar_state="expanded"
)
def load_custom_css(file_path):
    with open(file_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
load_custom_css("assets/css/styles.css")

# tracking and monitoring
def initialize_session_state():
    if 'enhancement_history' not in st.session_state:
        st.session_state.enhancement_history = []
    if 'current_session_id' not in st.session_state:
        st.session_state.current_session_id = None
    if 'processing_stats' not in st.session_state:
        st.session_state.processing_stats = {
            'total_images': 0,
            'successful_enhancements': 0,
            'failed_enhancements': 0
        }

def get_api_key():
    try:
        return st.secrets["GEMINI_API_KEY"]
    except:
        api_key = st.text_input(
            "🔑 Enter your Google Gemini API Key:",
            type="password",
            help="Get your API key from https://makersuite.google.com/app/apikey"
        )
        if not api_key:
            st.warning("Please enter your Gemini API key to continue.")
            st.stop()
        return api_key

def display_header():
    st.markdown(f'<h1 class="main-header">{CONFIG["app"]["welcome_header"]}</h1>', unsafe_allow_html=True)
    st.markdown(CONFIG["app"]["welcome_subtitle"])

    tab1, tab2, tab3, tab4 = st.tabs(CONFIG["tabs"])
    return tab1, tab2, tab3, tab4

def display_sidebar():
    """sidebar with settings and information."""
    st.sidebar.markdown(CONFIG["sidebar"]["settings"])
    
    # Image configuration
    st.sidebar.markdown(CONFIG["sidebar"]["image_settings"])
    
    max_size = st.sidebar.slider(CONFIG["sidebar"]["image_settings_slider_title_size"], CONFIG["sidebar"]["image_settings_slider_min_size"], CONFIG["sidebar"]["image_settings_slider_max_size"], CONFIG["sidebar"]["image_settings_slider_size"], 128)
    
    quality = st.sidebar.slider(CONFIG["sidebar"]["image_settings_slider_title_quality"], CONFIG["sidebar"]["image_settings_slider_min_quality"], CONFIG["sidebar"]["image_settings_slider_max_quality"], CONFIG["sidebar"]["image_settings_slider_quality"], 5)

    
    # Processing options
    st.sidebar.markdown(CONFIG["sidebar"]["processing_options"])
    max_retries = st.sidebar.slider(CONFIG["sidebar"]["processing_options_slider_title_retry"], CONFIG["sidebar"]["processing_options_slider_min_retry"], CONFIG["sidebar"]["processing_options_slider_max_retry"], CONFIG["sidebar"]["processing_options_slider_retry"])
    
    image_config = ImageConfig(
        max_size=(max_size, max_size),
        quality=quality
    )
    
    gemini_config = GeminiConfig(
        max_retries=max_retries
    )
    
    return image_config, gemini_config

def get_prompt_for_photopro(category: str = None) -> str:
    """
    Simple function to get a prompt.
    
    Args:
        category (str): Optional category name. If None, selects from any category.
        
    Returns:
        str: A prompt for photo enhancement
    """
    selector = PhotoPromptSelector()
    
    if category:
        prompt = selector.get_random_prompt(category)
        if prompt is None:
            # if specified category doesn't exist
            _, prompt = selector.get_random_prompt_any_category()
        return prompt
    else:
        # Get random prompt from any category
        _, prompt = selector.get_random_prompt_any_category()
        return prompt

def display_prompt_selector(selector_id):
    st.markdown(f'<div class="section-header">{CONFIG["prompts"]["enhancement_category_label"]}</div>', unsafe_allow_html=True)
    
    prompt_selector = PhotoPromptSelector()
    category_names = get_category_display_names()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Category selection
        selected_category_display = st.selectbox(
            CONFIG["prompts"]["enhancement_category_label"],
            options=list(category_names.values()),
            help=CONFIG["prompts"]["enhancement_category_help"],
            key=selector_id
        )
        
        # Get category name
        selected_category = None
        for internal_name, display_name in category_names.items():
            if display_name == selected_category_display:
                selected_category = internal_name
                break
    
    with col2:
        # Random prompt selection
        use_random = st.button(CONFIG["prompts"]["random_button"], help=CONFIG["prompts"]["random_button_help"],key=selector_id+"_button")
    
    # Get prompt
    if use_random:
        prompt = prompt_selector.get_random_prompt(selected_category)
    else:
        available_prompts = prompt_selector.get_category_prompts(selected_category)
        if available_prompts:
            prompt = st.selectbox(
                CONFIG["prompts"]["select_prompt_label"],
                options=available_prompts,
                format_func=lambda x: x[:100] + "..." if len(x) > 100 else x,
                key=selector_id+"_all"
            )
        else:
            prompt = get_prompt_for_photopro(selected_category)
    
    # Custom prompt option
    st.markdown(CONFIG["prompts"]["custom_prompt_title"])
    custom_prompt = st.text_area(
        CONFIG["prompts"]["custom_prompt_input"],
        placeholder=CONFIG["prompts"]["custom_prompt_placeholder"],
        height=100,
        key=selector_id+"_text"
    )
    
    final_prompt = custom_prompt if custom_prompt.strip() else prompt
    
    # Display selected prompt
    if final_prompt:
        st.markdown('<div class="enhancement-card">', unsafe_allow_html=True)
        st.markdown(f"**Selected Prompt:** {final_prompt}")
        st.markdown('</div>', unsafe_allow_html=True)
    
    return final_prompt

def process_uploaded_images(uploaded_files: List, prompt: str, api_key: str, 
                          image_config: ImageConfig, gemini_config: GeminiConfig):
    if not uploaded_files:
        st.warning(CONFIG["warning"]["upload"])
        return
    
    if not prompt:
        st.error(CONFIG["error"]["prompt"])
        return
    
    # temporary directory for processing
    with tempfile.TemporaryDirectory() as temp_dir:
        try:
            engine = GeminiEnhancementEngine(api_key, gemini_config, image_config)
            
            results = []
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            for i, uploaded_file in enumerate(uploaded_files):
                # progress
                progress = (i + 1) / len(uploaded_files)
                progress_bar.progress(progress)
                status_text.text(f"Processing {uploaded_file.name}... ({i+1}/{len(uploaded_files)})")
                
                # Save uploaded file temporarily
                temp_path = os.path.join(temp_dir, uploaded_file.name)
                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.getbuffer())
                
                try:
                    # Enhance
                    result = engine.enhance_image(temp_path, prompt, temp_dir)
                    result['original_filename'] = uploaded_file.name
                    result['success'] = True
                    results.append(result)
                    
                    # stats
                    st.session_state.processing_stats['successful_enhancements'] += 1
                    
                except Exception as e:
                    st.error(f"Failed to enhance {uploaded_file.name}: {str(e)}")
                    results.append({
                        'original_filename': uploaded_file.name,
                        'error': str(e),
                        'success': False
                    })
                    st.session_state.processing_stats['failed_enhancements'] += 1
            
            # Clear
            progress_bar.empty()
            status_text.empty()
            
            # stats
            st.session_state.processing_stats['total_images'] += len(uploaded_files)
            
            display_enhancement_results(results)
            
            # history
            st.session_state.enhancement_history.extend(results)
            
        except Exception as e:
            st.error(f"Processing failed: {str(e)}")

def display_enhancement_results(results: List[dict]):
    successful_results = [r for r in results if r.get('success', False)]
    failed_results = [r for r in results if not r.get('success', False)]
    
    if successful_results:
        st.markdown('<div class="success-message">', unsafe_allow_html=True)
        st.markdown(f"✅ Successfully enhanced {len(successful_results)} image(s)!")
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Display enhanced images
        for result in successful_results:
            st.markdown(f"### 🖼️ Enhanced: {result['original_filename']}")
            
            # Show before/after if possible
            col1, col2 = st.columns(2)
            
            with col2:
                if result['enhanced_images']:
                    enhanced_img_path = result['enhanced_images'][0]['path']
                    st.image(enhanced_img_path, caption="Enhanced Image", use_container_width =True)
                    
                    # Download button
                    with open(enhanced_img_path, "rb") as file:
                        st.download_button(
                            label="📥 Download Enhanced Image",
                            data=file.read(),
                            file_name=f"enhanced_{result['original_filename']}",
                            mime="image/png"
                        )
            
            # metadata
            with st.expander("📊 Enhancement Details"):
                st.json({
                    'processing_time': f"{result.get('processing_time_seconds', 0):.2f} seconds",
                    'session_id': result.get('session_id', 'N/A'),
                    'timestamp': result.get('timestamp', 'N/A'),
                    'image_info': result.get('enhanced_images', [{}])[0] if result.get('enhanced_images') else {}
                })
    
    if failed_results:
        st.markdown('<div class="error-message">', unsafe_allow_html=True)
        st.markdown(f"❌ Failed to enhance {len(failed_results)} image(s)")
        for result in failed_results:
            st.markdown(f"- {result['original_filename']}: {result.get('error', 'Unknown error')}")
        st.markdown('</div>', unsafe_allow_html=True)

def display_batch_processing_tab():
    st.markdown(f'<div class="section-header">{CONFIG["images"]["uplaod_images_header"]}</div>', unsafe_allow_html=True)
    
    uploaded_files = st.file_uploader(
        CONFIG["images"]["uplaod_images_title"],
        type=['png', 'jpg', 'jpeg', 'webp'],
        accept_multiple_files=True,
        help=CONFIG["images"]["uplaod_images_help"]
    )
    
    if uploaded_files:
        st.success(f"Uploaded {len(uploaded_files)} image(s)")
        
        # thumbnails
        cols = st.columns(min(len(uploaded_files), 5))
        for i, file in enumerate(uploaded_files[:5]):
            with cols[i]:
                st.image(file, caption=file.name, use_container_width =True)
        
        if len(uploaded_files) > 5:
            st.info(f"... and {len(uploaded_files) - 5} more images")
    
    return uploaded_files

def display_analytics_tab():
    st.markdown(f'<div class="section-header">{CONFIG["monitor"]["monitoring_header"]}</div>', unsafe_allow_html=True)
    
    # Processing statistics
    stats = st.session_state.processing_stats
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric(CONFIG["monitor"]["total_images"], stats['total_images'])
    
    with col2:
        st.metric(CONFIG["monitor"]["successful_enhancements"], stats['successful_enhancements'])
    
    with col3:
        st.metric(CONFIG["monitor"]["failed_enhancements"], stats['failed_enhancements'])
    
    # Success rate
    if stats['total_images'] > 0:
        success_rate = (stats['successful_enhancements'] / stats['total_images']) * 100
        st.metric("Success Rate", f"{success_rate:.1f}%")
    
    # history
    if st.session_state.enhancement_history:
        st.markdown(CONFIG["monitor"]["history_header"])
        
        for result in st.session_state.enhancement_history[-10:]:  # Show last 10
            with st.expander(f"🖼️ {result.get('original_filename', 'Unknown')} - {result.get('timestamp', 'N/A')[:19]}"):
                st.json(result)
    
    # Clear history
    if st.button(CONFIG["monitor"]["history_clear"]):
        st.session_state.enhancement_history = []
        st.session_state.processing_stats = {
            'total_images': 0,
            'successful_enhancements': 0,
            'failed_enhancements': 0
        }
        st.success(CONFIG["monitor"]["history_clear_res"])

def display_about_tab():
    # About PhotoPro
    st.markdown(f'<div class="section-header">{CONFIG["about_us"]["header"]}</div>', unsafe_allow_html=True)
    
    st.markdown(ABOUT)

def main():
    initialize_session_state()
    api_key = get_api_key()
    
    # tabs
    tab1, tab2, tab3, tab4 = display_header()
    
    # sidebar
    image_config, gemini_config= display_sidebar()
    
    # Tab 1: One Image
    with tab1:
        st.markdown(f'<div class="section-header">{CONFIG["images"]["single_image_process"]}</div>', unsafe_allow_html=True)
        
        # image uploader
        uploaded_file = st.file_uploader(
            CONFIG["images"]["uplaod_image_label"],
            type=['png', 'jpg', 'jpeg', 'webp'],
            help=CONFIG["images"]["uplaod_image_help"]
        )
        
        if uploaded_file:
            # original image
            col1, col2 = st.columns(2)
            with col1:
                st.image(uploaded_file, caption=CONFIG["images"]["original_image_caption"], use_container_width =True)
        
        # Prompt
        prompt = display_prompt_selector("prompt")
        
        # Main Process
        if st.button(CONFIG["main"]["process_action"], type="primary"):
            if uploaded_file and prompt:
                process_uploaded_images([uploaded_file], prompt, api_key, image_config, gemini_config)
    
    # Tab 2: Processing a Group of Images
    with tab2:
        uploaded_files = display_batch_processing_tab()
        
        # Prompt
        prompt = display_prompt_selector("batch_prompt")
        
        # main process
        if st.button(CONFIG["main"]["process_action_batch"], type="primary"):
            if uploaded_files and prompt:
                process_uploaded_images(uploaded_files, prompt, api_key, image_config, gemini_config)
    
    # Tab 3: Monitoring
    with tab3:
        display_analytics_tab()
    
    # Tab 4: About US 
    with tab4:
        display_about_tab()

if __name__ == "__main__":
    main()