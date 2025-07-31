import streamlit as st
import numpy as np
import cv2 as cv
from PIL import Image
from io import BytesIO
import os
from streamlit_webrtc import webrtc_streamer, VideoTransformerBase
import av

# ---------- CONFIG ----------
PROTOTXT_PATH = r"C:\Users\jyoth\OneDrive\Desktop\projects\colourization\model\colorization_deploy_v2.prototxt"
CAFFEMODEL_PATH = r"C:\Users\jyoth\OneDrive\Desktop\projects\colourization\model\colorization_release_v2.caffemodel"
KERNEL_PATH = r"C:\Users\jyoth\OneDrive\Desktop\projects\colourization\model\pts_in_hull.npy"
# ----------------------------

st.set_page_config(page_title="PaintBack", layout="centered", page_icon="🎨")

st.markdown("""
    <style>
        html, body, [class*="css"]  {
            background-color: #fdf6f0;
            color: #4a4a4a;
            font-family: 'Trebuchet MS', sans-serif;
        }
        .css-18ni7ap {
            background-color: #ffe5ec;
            padding: 1em;
            border-radius: 10px;
        }
        .stButton button {
            background-color: #e0bbf4;
            color: black;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🎨 PaintBack")
st.subheader("🧠 AI-Powered Color for the Moments that Matter.")
st.markdown("💖 *Because every memory deserves a splash of color.*")

st.markdown("---")

st.markdown("#### Choose your input method:")

option = st.radio("Select input source", ["📁 Upload an Image", "📷 Use Webcam"], horizontal=True)

# ---------- MODEL LOADING ----------
@st.cache_resource
def load_model():
    net = cv.dnn.readNetFromCaffe(PROTOTXT_PATH, CAFFEMODEL_PATH)
    pts_in_hull = np.load(KERNEL_PATH)
    pts_in_hull = pts_in_hull.transpose().reshape(2, 313, 1, 1)
    net.getLayer(net.getLayerId("class8_ab")).blobs = [pts_in_hull.astype(np.float32)]
    net.getLayer(net.getLayerId("conv8_313_rh")).blobs = [np.full([1, 313], 2.606, np.float32)]
    return net

net = load_model()

# ---------- COLORIZATION FUNCTION ----------
def colorize_image(input_image):
    rgb = cv.cvtColor(input_image, cv.COLOR_BGR2RGB)
    img_rgb = rgb.astype(np.float32) / 255.0
    img_lab = cv.cvtColor(img_rgb, cv.COLOR_RGB2Lab)
    img_l = img_lab[:, :, 0]
    H_orig, W_orig = img_rgb.shape[:2]

    img_rs = cv.resize(img_rgb, (1280,720))
    img_lab_rs = cv.cvtColor(img_rs, cv.COLOR_RGB2Lab)
    img_l_rs = img_lab_rs[:, :, 0]
    img_l_rs -= 50

    net.setInput(cv.dnn.blobFromImage(img_l_rs))
    ab_dec = net.forward()[0, :, :, :].transpose((1, 2, 0))
    ab_dec_us = cv.resize(ab_dec, (W_orig, H_orig))

    img_lab_out = np.concatenate((img_l[:, :, np.newaxis], ab_dec_us), axis=2)
    img_bgr_out = np.clip(cv.cvtColor(img_lab_out, cv.COLOR_Lab2BGR), 0, 1) * 255
    return img_bgr_out.astype(np.uint8)

# ---------- IMAGE UPLOAD ----------
if option == "📁 Upload an Image":
    uploaded_file = st.file_uploader("Upload a grayscale image (JPG, PNG)", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        bgr = cv.imdecode(file_bytes, cv.IMREAD_COLOR)
        colorized = colorize_image(bgr)

        st.markdown("#### 🖼️ Here's the result:")

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Original")
            st.image(cv.cvtColor(bgr, cv.COLOR_BGR2RGB), channels="RGB")

        with col2:
            st.subheader("🎨 Colorized")
            st.image(cv.cvtColor(colorized, cv.COLOR_BGR2RGB), channels="RGB")

    # Download button
        buf = BytesIO()
        Image.fromarray(cv.cvtColor(colorized, cv.COLOR_BGR2RGB)).save(buf, format="PNG")
        st.download_button("💾 Save Your Colorized Image", buf.getvalue(), "colorized.png", mime="image/png")

# ---------- WEBCAM INPUT ----------
if option == "📷 Use Webcam":
    class VideoTransformer(VideoTransformerBase):
        def transform(self, frame: av.VideoFrame) -> np.ndarray:
            img = frame.to_ndarray(format="bgr24")
            try:
                colorized = colorize_image(img)
                return colorized
            except:
                return img

    st.warning("📸 Webcam might take a few seconds to initialize.")
    webrtc_streamer(key="colorize", video_transformer_factory=VideoTransformer)
