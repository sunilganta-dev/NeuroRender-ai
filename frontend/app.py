import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(page_title="NeuroRender.ai", layout="centered")
st.title("🧠 NeuroRender.ai - Multimodal Image Generator")

st.markdown("""
Welcome to **NeuroRender.ai**, an agentic AI-powered platform for GPU-optimized, LLM-controlled image generation.

👉 Enter a creative prompt and get a custom-generated image using cutting-edge diffusion models.
""")

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

# User input
prompt = st.text_area("Enter your prompt:", placeholder="A futuristic city on Mars at sunset...")
generate_btn = st.button("Generate Image")

# Server URL
BACKEND_URL = "http://127.0.0.1:8000/generate"
GPU_STATS_URL = "http://127.0.0.1:8000/gpu-status"

if generate_btn and prompt:
    with st.spinner("Refining your prompt and generating image..."):
        try:
            response = requests.post(BACKEND_URL, json={"prompt": prompt})
            if response.status_code == 200:
                result = response.json()
                image_data = requests.get(result["image_url"]).content
                image = Image.open(BytesIO(image_data))
                st.image(image, caption="🎨 Generated Image", use_column_width=True)

                # Save in session
                st.session_state.history.append((prompt, image))

                # Download Image
                buffered = BytesIO()
                image.save(buffered, format="PNG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                download_link = f'<a href="data:file/png;base64,{img_str}" download="generated_image.png">📥 Download Image</a>'
                st.markdown(download_link, unsafe_allow_html=True)
                st.success("✅ Image generated and ready to download!")
            else:
                st.error(f"❌ Error: {response.json().get('detail', 'Image generation failed')}")
        except Exception as e:
            st.error(f"🚨 Server error: {e}")

# GPU Status
st.markdown("### 🔋 GPU Status")
try:
    gpu_response = requests.get(GPU_STATS_URL)
    if gpu_response.status_code == 200:
        gpu_info = gpu_response.json()
        st.json(gpu_info)
    else:
        st.warning("⚠️ Could not fetch GPU status.")
except Exception as e:
    st.warning(f"⚠️ Error fetching GPU status: {e}")

# Image History
if st.session_state.history:
    st.markdown("### 🕘 Image History")
    for i, (p, img) in enumerate(reversed(st.session_state.history[-5:]), 1):
        st.image(img, caption=f"📝 Prompt {i}: {p}", width=300)

st.markdown("---")
st.caption("Built using FastAPI, PyTorch, Streamlit, and LangChain.")
