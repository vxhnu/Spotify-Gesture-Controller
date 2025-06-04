# 🎵 Spotify Desktop Gesture Controller

Control your Spotify Desktop App using just your hand gestures via webcam—no keyboard or mouse needed.

> Built with Python, MediaPipe, OpenCV, and PyAutoGUI.  
> Part of the **AirPointer** initiative for contactless human-computer interaction.

---

## 🚀 Features

- 👋 Real-time hand tracking using MediaPipe
- 🖥️ Control Spotify playback on Windows desktop
- 📷 Webcam-based gesture recognition
- 🎛️ Supported Controls:
  - **Open palm** → Play/Pause
  - **Fist** → Next Track
  - **Two fingers (index + middle)** → Volume Up
  - **Ring + pinky** → Volume Down
  - **Only pinky** → Previous Track
  - **Thumb + index** → Shuffle

- ⏱️ Built-in cooldown to avoid repeated gestures
- 🖼️ Gesture title overlay in live video feed

---

## 🧰 Tech Stack

- **Python 3**
- [OpenCV](https://opencv.org/)
- [MediaPipe Hands](https://google.github.io/mediapipe/solutions/hands)
- [PyAutoGUI](https://pyautogui.readthedocs.io/)
- `cv2.putText()` for live gesture feedback

---

## 📁 Project Structure

spotify_gesture_controller/
├── main.py # Main gesture controller script
├── README.md # Project overview and setup instructions
├── requirements.txt # Python dependencies