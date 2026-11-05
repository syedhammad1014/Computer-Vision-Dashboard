# Computer Vision Dashboard

A real-time object detection and visual analytics dashboard built with **Streamlit**, **OpenCV**, and custom computer vision workflows utilizing **CVAT** (Computer Vision Annotation Tool).

## Features
- **Multi-Source Detection:** Process static images, video files, or live webcam streams.
- **Custom Annotation Workflow:** Compatible with CVAT bounding box annotations (XML/JSON/YOLO formats).
- **Interactive Threshold Controls:** Dynamic confidence sliders, intersection-over-union (IoU) filtering, and class filtering.
- **Visual Analytics:** Real-time object count metrics, bounding box overlays, and detection summary tables.

## Installation & Running
```bash
git clone https://github.com/syedhammad1014/Computer-Vision-Dashboard.git
cd Computer-Vision-Dashboard
pip install -r requirements.txt
streamlit run app.py
```

## Technologies
- **Python 3.10+**
- **Streamlit**
- **OpenCV (cv2)**
- **NumPy & Pillow**
- **CVAT Annotation Integration**
