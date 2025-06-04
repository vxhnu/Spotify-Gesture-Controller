# 🎵 Spotify Desktop Gesture Controller

Control your Spotify Desktop App using just your hand gestures via webcam—no keyboard or mouse needed.

> Built with Python, MediaPipe, OpenCV, and PyAutoGUI.  
> Part of the **AirPointer** initiative for contactless human-computer interaction.

---

## ✨ Features

* 👋 Detects hand gestures using webcam
* 🎶 Controls Spotify (Play/Pause, Next, Previous, Volume Up/Down, Shuffle)
* 💻 Simple graphical interface (Start/Exit buttons)
* 🚀 Automatically launches Spotify on start
* 🪟 Built for Windows (Python executable with GUI)

---

## 📸 Recognized Gestures

| Gesture (Fingers Up) | Action         |
| -------------------- | -------------- |
| 11111                | Play/Pause     |
| 00000                | Next Track     |
| 11100                | Previous Track |
| 01100                | Volume Up      |
| 10000                | Volume Down    |
| 11000                | Shuffle        |

> Tip: "1" means the finger is up, "0" means it's folded. Order: Thumb, Index, Middle, Ring, Pinky.

---

## 🛠️ Technologies Used

* Python
* OpenCV
* MediaPipe
* Tkinter (GUI)
* PyAutoGUI (for keyboard events)

---

## 📦 How to Use

1. **Install Dependencies**
   Install required Python packages:

   ```bash
   pip install opencv-python mediapipe pyautogui
   ```

2. **Run the App**

   ```bash
   python main.py
   ```

3. **Build the Executable (Optional)**
   If you want to generate a Windows `.exe`:

   ```bash
   pyinstaller --noconfirm --onefile --windowed --icon=icon.ico main.py
   ```

4. **Distribute**
   Share the `.exe` file with others. No Python installation required on their side.

---

## 🧠 How It Works

* The app uses **MediaPipe** to detect hand landmarks from the webcam.
* Based on the position of fingertips, a gesture is mapped to a specific media control.
* **PyAutoGUI** sends the equivalent keyboard command to control Spotify.
* **Tkinter** provides a minimal, user-friendly GUI to start or stop the application.

---

## 📌 Notes

* Make sure Spotify is installed and available in the system PATH. The app attempts to launch Spotify using the `start` command or system-detected path.
* Webcam access is required.
* ESC key exits the gesture window.

---

## 👨‍💻 Author

**\[VISHNU RAMESHAN]**
* If you find this project useful or have suggestions, feel free to reach out or contribute.
* gmail - vishnu.rameshan03@gmail.com

---

