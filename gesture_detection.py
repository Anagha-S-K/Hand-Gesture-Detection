import cv2
import numpy as np
import streamlit as st
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python.vision import GestureRecognizer, GestureRecognizerOptions
from mediapipe.tasks import python
from mediapipe import solutions as mp_solutions
from mediapipe.framework.formats import landmark_pb2


# Setup
mp_drawing = mp_solutions.drawing_utils
mp_drawing_styles = mp_solutions.drawing_styles


st.set_page_config(page_title="Hand Gesture Detection", layout="wide")
st.title("Real-time Hand Gesture Recognition")
st.caption("Using pre-trained models")

# Load the model
MODEL_PATH = "gesture_recognizer.task"

base_options = python.BaseOptions(model_asset_path=MODEL_PATH)
options = vision.GestureRecognizerOptions(base_options=base_options)
recognizer = vision.GestureRecognizer.create_from_options(options)

# Streamlit layout
st.sidebar.header("Configuration")
run = st.sidebar.checkbox("Start Webcam")

col1, col2 = st.columns([1, 1])
with col1:
    FRAME_WINDOW = st.image([])
with col2:
    LABEL_TEXT = st.markdown("")

# Webcam
cap = cv2.VideoCapture(0)

while run:
    success, frame = cap.read()
    if not success:
        st.error("Failed to access webcam.")
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Convert to MP Image
    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)

    # Inference
    result = recognizer.recognize(mp_image)
    gesture = result.gestures[0][0] if result.gestures else None

        # Draw landmarks if detected
    if result.hand_landmarks:
        for hand_landmarks in result.hand_landmarks:
        # Manually convert each point to the protobuf format
            proto_landmarks = [
                landmark_pb2.NormalizedLandmark(x=lm.x, y=lm.y, z=lm.z)
                for lm in hand_landmarks
        ]

            landmark_list_proto = landmark_pb2.NormalizedLandmarkList(landmark=proto_landmarks)

            mp_drawing.draw_landmarks(
                rgb_frame,
                landmark_list_proto,
                mp_solutions.hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style()
        )

    with col1:
        FRAME_WINDOW.image(rgb_frame)

    with col2:
        if gesture:
            LABEL_TEXT.markdown(
                f"## Detected Gesture: **{gesture.category_name}**  \n"
                f"### Confidence: **{gesture.score * 100:.2f}%**"
            )
        else:
            LABEL_TEXT.markdown("## No recognizable gesture")

cap.release()