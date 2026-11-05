import streamlit as st
import numpy as np
from PIL import Image
from detector import ObjectDetector

st.set_page_config(page_title="Computer Vision Dashboard", page_icon="👁️", layout="wide")

st.title("👁️ Computer Vision & Object Detection Dashboard")
st.markdown("Real-time visual inspection, bounding-box detection, and CVAT-compatible annotation processing.")

detector = ObjectDetector()

confidence = st.sidebar.slider("Detection Confidence Threshold", min_value=0.1, max_value=1.0, value=0.5, step=0.05)

uploaded_file = st.sidebar.file_uploader("Upload Image for Detection", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)
        
    with col2:
        st.subheader("Detected Objects")
        processed_img, detections = detector.detect(image, conf_threshold=confidence)
        st.image(processed_img, use_container_width=True)
        
    st.divider()
    st.subheader(f"📊 Detection Summary ({len(detections)} objects found)")
    st.table(detections)
else:
    st.info("👈 Upload an image in the sidebar to begin real-time object detection.")
