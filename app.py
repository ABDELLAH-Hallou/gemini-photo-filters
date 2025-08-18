import streamlit as st
import os
import tempfile
import zipfile
from pathlib import Path
from datetime import datetime
from typing import List, Optional, Dict, Any, Tuple
import time
import yaml
from engine import (
    GeminiEnhancementEngine,
    GeminiConfig
)
from utils.about import ABOUT
from utils.filters import ImageFilterManager
from utils.image import (
    ImageConfig
)
    
class PhotoProApp:
    def __init__(self, config_path: str = "data.yaml"):
        self.config = self._load_config(config_path)
        self.image_filter_manager = ImageFilterManager()
        self._setup_streamlit_config()
        self._load_custom_css()
        self._initialize_session_state()
    
    def _load_config(self, path: str) -> Dict[str, Any]:
        with open(path, "r", encoding="utf-8") as file:
            return yaml.safe_load(file)
    
    def _setup_streamlit_config(self) -> None:
        st.set_page_config(
            page_title=self.config["app"]["page_title"],
            page_icon=self.config["app"]["page_icon"],
            layout="wide",
            initial_sidebar_state="expanded"
        )
    
    def _load_custom_css(self, file_path: str = "assets/css/styles.css") -> None:
        try:
            with open(file_path) as f:
                st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
        except FileNotFoundError:
            st.warning(f"CSS file not found: {file_path}")
    
    def _initialize_session_state(self)->None:
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
        if 'active_filters' not in st.session_state:
            st.session_state.active_filters = {}
    
    def _get_api_key(self)->str:
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
    
    def _display_header(self) -> Tuple[Any, Any, Any, Any]:
        st.markdown(
            f'<h1 class="main-header">{self.config["app"]["welcome_header"]}</h1>', 
            unsafe_allow_html=True
        )
        st.markdown(self.config["app"]["welcome_subtitle"])
        
        tab1, tab2, tab3, tab4 = st.tabs(self.config["tabs"])
        return tab1, tab2, tab3, tab4
    
    def _display_sidebar(self) -> Tuple[ImageConfig, GeminiConfig]:
        """sidebar with settings and information."""
        st.sidebar.markdown(self.config["sidebar"]["settings"])
        
        # Image configuration
        st.sidebar.markdown(self.config["sidebar"]["image_settings"])
        
        max_size = st.sidebar.slider(
            self.config["sidebar"]["image_settings_slider_title_size"], 
            self.config["sidebar"]["image_settings_slider_min_size"], 
            self.config["sidebar"]["image_settings_slider_max_size"], 
            self.config["sidebar"]["image_settings_slider_size"], 
            128
        )
        
        quality = st.sidebar.slider(
            self.config["sidebar"]["image_settings_slider_title_quality"], 
            self.config["sidebar"]["image_settings_slider_min_quality"], 
            self.config["sidebar"]["image_settings_slider_max_quality"], 
            self.config["sidebar"]["image_settings_slider_quality"], 
            5
        )
        
        # Processing options
        st.sidebar.markdown(self.config["sidebar"]["processing_options"])
        max_retries = st.sidebar.slider(
            self.config["sidebar"]["processing_options_slider_title_retry"], 
            self.config["sidebar"]["processing_options_slider_min_retry"], 
            self.config["sidebar"]["processing_options_slider_max_retry"], 
            self.config["sidebar"]["processing_options_slider_retry"]
        )
        
        image_config = ImageConfig(
            max_size=(max_size, max_size),
            quality=quality
        )
        
        gemini_config = GeminiConfig(
            max_retries=max_retries
        )
        
        return image_config, gemini_config
    
    
    def _process_uploaded_images(self, uploaded_files: List, prompt: str, api_key: str,  image_config: ImageConfig, gemini_config: GeminiConfig)->None:
        if not uploaded_files:
            st.warning(self.config["warning"]["upload"])
            return
        
        if not prompt:
            st.error(self.config["error"]["prompt"])
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
                
                self._display_enhancement_results(results)
                
                # history
                st.session_state.enhancement_history.extend(results)
                
            except Exception as e:
                st.error(f"Processing failed: {str(e)}")
    
    def _display_enhancement_results(self, results: List[Dict[str, Any]]) -> None:
        successful_results = [r for r in results if r.get('success', False)]
        failed_results = [r for r in results if not r.get('success', False)]
        
        if successful_results:
            st.markdown('<div class="success-message">', unsafe_allow_html=True)
            st.markdown(f"✅ Successfully enhanced {len(successful_results)} image(s)!")
            st.markdown('</div>', unsafe_allow_html=True)
            
            for result in successful_results:
                st.markdown(f"### 🖼️ Enhanced: {result['original_filename']}")
                
                col1, col2 = st.columns(2)
                
                with col2:
                    if result['enhanced_images']:
                        enhanced_img_path = result['enhanced_images'][0]['path']
                        st.image(enhanced_img_path, caption="Enhanced Image", use_container_width=True)
                        
                        with open(enhanced_img_path, "rb") as file:
                            st.download_button(
                                label="📥 Download Enhanced Image",
                                data=file.read(),
                                file_name=f"enhanced_{result['original_filename']}",
                                mime="image/png"
                            )
                
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
    
    def _display_batch_processing_tab(self) -> List:
        st.markdown(
            f'<div class="section-header">{self.config["images"]["uplaod_images_header"]}</div>', 
            unsafe_allow_html=True
        )
        
        uploaded_files = st.file_uploader(
            self.config["images"]["uplaod_images_title"],
            type=['png', 'jpg', 'jpeg', 'webp'],
            accept_multiple_files=True,
            help=self.config["images"]["uplaod_images_help"]
        )
        
        if uploaded_files:
            st.success(f"Uploaded {len(uploaded_files)} image(s)")
            
            cols = st.columns(min(len(uploaded_files), 5))
            for i, file in enumerate(uploaded_files[:5]):
                with cols[i]:
                    st.image(file, caption=file.name, use_container_width=True)
            
            if len(uploaded_files) > 5:
                st.info(f"... and {len(uploaded_files) - 5} more images")
        
        return uploaded_files
    
    def _display_analytics_tab(self) -> None:
        st.markdown(
            f'<div class="section-header">{self.config["monitor"]["monitoring_header"]}</div>', 
            unsafe_allow_html=True
        )
        
        stats = st.session_state.processing_stats
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(self.config["monitor"]["total_images"], stats['total_images'])
        
        with col2:
            st.metric(self.config["monitor"]["successful_enhancements"], stats['successful_enhancements'])
        
        with col3:
            st.metric(self.config["monitor"]["failed_enhancements"], stats['failed_enhancements'])
        
        if stats['total_images'] > 0:
            success_rate = (stats['successful_enhancements'] / stats['total_images']) * 100
            st.metric("Success Rate", f"{success_rate:.1f}%")
        
        if st.session_state.enhancement_history:
            st.markdown(self.config["monitor"]["history_header"])
            
            for result in st.session_state.enhancement_history[-10:]:
                with st.expander(
                    f"🖼️ {result.get('original_filename', 'Unknown')} - "
                    f"{result.get('timestamp', 'N/A')[:19]}"
                ):
                    st.json(result)
        
        if st.button(self.config["monitor"]["history_clear"]):
            st.session_state.enhancement_history = []
            st.session_state.processing_stats = {
                'total_images': 0,
                'successful_enhancements': 0,
                'failed_enhancements': 0
            }
            st.success(self.config["monitor"]["history_clear_res"])
    
    def _display_about_tab(self) -> None:
        st.markdown(
            f'<div class="section-header">{self.config["about_us"]["header"]}</div>', 
            unsafe_allow_html=True
        )
        st.markdown(ABOUT)
    
    def _display_filter_controls(self) -> Dict[str, Any]:
        st.markdown("### 🎨 Image Filters Configuration")
        
        selected_filters = []
        filter_categories = self.image_filter_manager.get_filter_categories()
        filter_parameters = self.image_filter_manager.get_all_parameters()
        
        for category, filters in filter_categories.items():
            with st.expander(category, expanded=False):
                cols = st.columns(2)
                for i, filter_name in enumerate(filters):
                    with cols[i % 2]:
                        if st.checkbox(
                            filter_name.replace('_', ' ').title(), 
                            key=f"filter_{filter_name}"
                        ):
                            selected_filters.append(filter_name)
        
        configured_filters = {}
        
        if selected_filters:
            st.markdown("### ⚙️ Filter Parameters")
            
            for filter_name in selected_filters:
                with st.expander(f"Configure {filter_name.replace('_', ' ').title()}", expanded=True):
                    params = {}
                    
                    if filter_name in filter_parameters:
                        filter_params = filter_parameters[filter_name]
                        
                        cols = st.columns(2)
                        col_idx = 0
                        
                        for param_name, options in filter_params.items():
                            with cols[col_idx % 2]:
                                if isinstance(options, dict) and options.get("type") == "slider":
                                    # slider
                                    params[param_name] = st.slider(
                                        f"{param_name.replace('_', ' ').title()} ({options['unit']})",
                                        min_value=options["min"],
                                        max_value=options["max"],
                                        value=options["default"],
                                        step=options["step"],
                                        key=f"{filter_name}_{param_name}"
                                    )
                                elif isinstance(options, dict) and options.get("type") == "number_input":
                                    # numbers
                                    params[param_name] = st.number_input(
                                        f"{param_name.replace('_', ' ').title()} ({options['unit']})",
                                        min_value=options["min"],
                                        max_value=options["max"],
                                        value=options["default"],
                                        key=f"{filter_name}_{param_name}"
                                    )
                                elif isinstance(options, dict) and options.get("type") == "text_input":
                                    # texts
                                    params[param_name] = st.text_input(
                                        param_name.replace('_', ' ').title(),
                                        value=options["default"],
                                        placeholder=options.get("placeholder", ""),
                                        key=f"{filter_name}_{param_name}"
                                    )
                                elif isinstance(options, list):
                                    # selection
                                    params[param_name] = st.selectbox(
                                        param_name.replace('_', ' ').title(),
                                        options,
                                        key=f"{filter_name}_{param_name}"
                                    )
                                else:
                                    params[param_name] = st.text_input(
                                        param_name.replace('_', ' ').title(),
                                        value=str(options),
                                        key=f"{filter_name}_{param_name}"
                                    )
                            col_idx += 1
                    
                    if not filter_parameters.get(filter_name):
                        params = {}
                    
                    configured_filters[filter_name] = params
        
        return configured_filters
    
    def _display_prompt_selector_with_filters(self, key_suffix: str = "") -> str:
        prompt_option = st.radio(
            "Choose prompt type:",
            ["Custom Prompt", "Filter-Based Prompt", "Combined Prompt"],
            key=f"prompt_type_{key_suffix}"
        )
        
        final_prompt = ""
        
        if prompt_option == "Custom Prompt":
            final_prompt = st.text_area(
                "Enter your custom prompt:",
                height=100,
                placeholder="Describe what you want to do with the image...",
                key=f"custom_prompt_{key_suffix}"
            )
        
        elif prompt_option == "Filter-Based Prompt":
            configured_filters = self._display_filter_controls()
            
            if configured_filters:
                final_prompt = self.image_filter_manager.combine_filter_prompts(configured_filters)
                
                if final_prompt:
                    with st.expander("Preview Combined Prompt", expanded=False):
                        st.text_area(
                            "Combined Filter Prompt:", 
                            value=final_prompt, 
                            height=200, 
                            disabled=True
                        )
            else:
                st.info("Select and configure filters above to generate the prompt.")
        
        elif prompt_option == "Combined Prompt":
            custom_prompt = st.text_area(
                "Enter your custom prompt:",
                height=100,
                placeholder="Describe additional modifications...",
                key=f"combined_custom_prompt_{key_suffix}"
            )
            
            configured_filters = self._display_filter_controls()
            filter_prompt = (
                self.image_filter_manager.combine_filter_prompts(configured_filters) 
                if configured_filters else ""
            )
            
            if custom_prompt and filter_prompt:
                final_prompt = f"{custom_prompt}\n\nAdditionally, apply these filters:\n{filter_prompt}"
            elif custom_prompt:
                final_prompt = custom_prompt
            elif filter_prompt:
                final_prompt = filter_prompt
            
            if final_prompt:
                with st.expander("Preview Combined Prompt", expanded=False):
                    st.text_area(
                        "Final Combined Prompt:", 
                        value=final_prompt, 
                        height=200, 
                        disabled=True
                    )
        
        return final_prompt
    
    def run(self) -> None:
        api_key = self._get_api_key()
        
        tab1, tab2, tab3, tab4 = self._display_header()
        
        image_config, gemini_config = self._display_sidebar()
        
        # Tab 1: Single Image Processing
        with tab1:
            st.markdown(
                f'<div class="section-header">{self.config["images"]["single_image_process"]}</div>', 
                unsafe_allow_html=True
            )
            
            uploaded_file = st.file_uploader(
                self.config["images"]["uplaod_image_label"],
                type=['png', 'jpg', 'jpeg', 'webp'],
                help=self.config["images"]["uplaod_image_help"]
            )
            
            if uploaded_file:
                col1, col2 = st.columns(2)
                with col1:
                    st.image(
                        uploaded_file, 
                        caption=self.config["images"]["original_image_caption"], 
                        use_container_width=True
                    )
            
            prompt = self._display_prompt_selector_with_filters("prompt")
            
            if st.button(self.config["main"]["process_action"], type="primary"):
                if uploaded_file and prompt:
                    self._process_uploaded_images(
                        [uploaded_file], prompt, api_key, image_config, gemini_config
                    )
        
        # Tab 2: Batch Processing
        with tab2:
            uploaded_files = self._display_batch_processing_tab()
            prompt = self._display_prompt_selector_with_filters("batch_prompt")
            
            if st.button(self.config["main"]["process_action_batch"], type="primary"):
                if uploaded_files and prompt:
                    self._process_uploaded_images(
                        uploaded_files, prompt, api_key, image_config, gemini_config
                    )
        
        # Tab 3: Monitoring
        with tab3:
            self._display_analytics_tab()
        
        # Tab 4: About US
        with tab4:
            self._display_about_tab()


def main():
    app = PhotoProApp()
    app.run()


if __name__ == "__main__":
    main()