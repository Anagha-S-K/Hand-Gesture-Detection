# ✋ Real-time Hand Gesture Detection using MediaPipe & Streamlit

This is a **real-time hand gesture recognition web app** built using **MediaPipe**, **Streamlit**, and **OpenCV**. It uses MediaPipe's **pre-trained `gesture_recognizer.task` model** to detect hand gestures from your webcam input, display landmark overlays, and output gesture predictions along with confidence scores — all inside an interactive browser interface.

---

## 🚀 Features

- ✅ **Real-time Webcam Feed**
- ✋ **Hand Landmark Detection** (21 key points per hand)
- 🧠 **Pre-trained Gesture Recognition** via `gesture_recognizer.task`
- 📈 **Live Confidence Score**
- 🎨 **Streamlit Interface with Sidebar Controls**
- 🔄 **Auto-flip Frame for Mirror View**

---

## 🧠 How It Works

1. Captures real-time video frames using OpenCV.
2. Converts frames to RGB format.
3. MediaPipe’s `GestureRecognizer` detects hand landmarks and predicts gestures.
4. Detected gesture name and confidence score are displayed.
5. Hand landmarks and connections are drawn over the video feed.

---

## 🛠️ Tech Stack

| Tool/Library     | Description                            |
|------------------|----------------------------------------|
| Python           | Core programming language              |
| Streamlit        | Web app framework                      |
| OpenCV           | Webcam access and image processing     |
| MediaPipe        | Landmark detection & gesture model     |

---


