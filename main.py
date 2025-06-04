# import cv2
# import mediapipe as mp
# import pyautogui
# import time

# # Initialize MediaPipe
# mp_drawing = mp.solutions.drawing_utils
# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(max_num_hands=1)

# # Cooldown to prevent multiple triggers
# cooldown = 1.5  # seconds
# last_action_time = 0

# # Gesture recognition from hand landmarks
# def recognize_gesture(landmarks):
#     fingers = []

#     # Thumb
#     if landmarks[4].x < landmarks[3].x:
#         fingers.append(1)
#     else:
#         fingers.append(0)

#     # Index, Middle, Ring, Pinky
#     for tip in [8, 12, 16, 20]:
#         if landmarks[tip].y < landmarks[tip - 2].y:
#             fingers.append(1)
#         else:
#             fingers.append(0)

#     # Gesture definitions
#     if fingers == [1, 1, 1, 1, 1]:
#         return "PlayPause"
#     elif fingers == [0, 0, 0, 0, 0]:
#         return "Next"
#     elif fingers == [1, 1, 1, 0, 0]:
#         return "Previous"
#     elif fingers == [1, 1, 0, 0, 0]:
#         return "VolumeUp"
#     elif fingers == [0, 1, 0, 0, 1]:
#         return "VolumeDown"
#     elif fingers == [1, 1, 0, 0, 0]:
#         return "Shuffle"
#     else:
#         return None

# # Map gestures to actions
# def perform_action(gesture):
#     global last_action_time
#     current_time = time.time()

#     if current_time - last_action_time < cooldown:
#         return

#     print(f"Gesture Detected: {gesture}")

#     if gesture == "PlayPause":
#         pyautogui.press("playpause")
#     elif gesture == "Next":
#         pyautogui.press("nexttrack")
#     elif gesture == "Previous":
#         pyautogui.press("prevtrack")
#     elif gesture == "VolumeUp":
#         pyautogui.press("volumeup")
#     elif gesture == "VolumeDown":
#         pyautogui.press("volumedown")
#     elif gesture == "Shuffle":
#         pyautogui.hotkey("ctrl", "s")

#     last_action_time = current_time

# # Start webcam
# cap = cv2.VideoCapture(0)
# print("Starting Spotify Gesture Controller... Press ESC to exit.")

# while cap.isOpened():
#     ret, frame = cap.read()
#     frame = cv2.flip(frame, 1)
#     rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     result = hands.process(rgb_frame)

#     if result.multi_hand_landmarks:
#         for hand_landmarks in result.multi_hand_landmarks:
#             mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
#             gesture = recognize_gesture(hand_landmarks.landmark)
#             if gesture:
#                 perform_action(gesture)
#                 cv2.putText(frame, f'Gesture: {gesture}', (10, 40),
#                             cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

#     cv2.imshow("Spotify Gesture Controller", frame)

#     if cv2.waitKey(5) & 0xFF == 27:  # ESC key
#         break

# cap.release()
# cv2.destroyAllWindows()



# _----------------------------------------------------------------------------------------------------------------------------
# main working code 


#!/usr/bin/env python3
# main.py: Gesture-based Spotify controller with Tkinter GUI
#
# Dependencies:
#   - psutil        (pip install psutil)
#   - opencv-python (pip install opencv-python)
#   - mediapipe     (pip install mediapipe)
#   - pyautogui     (pip install pyautogui)
#   - (tkinter is usually included with Python on Windows)


# import cv2
# import mediapipe as mp
# import pyautogui
# import time

# mp_hands = mp.solutions.hands
# mp_drawing = mp.solutions.drawing_utils

# hands = mp_hands.Hands(static_image_mode=False,
#                        max_num_hands=1,
#                        min_detection_confidence=0.7,
#                        min_tracking_confidence=0.7)

# TIP_IDS = [4, 8, 12, 16, 20]

# GESTURES = {
#     "11111": "PlayPause",
#     "00000": "Next",
#     "11100": "Previous",
#     "01100": "VolumeUp",
#     "10000": "VolumeDown",
#     "01111": "Shuffle"
# }

# cooldown = 1.5
# last_action_time = 0

# def detect_fingers(landmarks):
#     fingers = []

#     # Thumb
#     fingers.append(1 if landmarks[TIP_IDS[0]].x > landmarks[TIP_IDS[0] - 1].x else 0)

#     # Other fingers
#     for id in range(1, 5):
#         fingers.append(1 if landmarks[TIP_IDS[id]].y < landmarks[TIP_IDS[id] - 2].y else 0)

#     return fingers

# def recognize_gesture(fingers):
#     pattern = ''.join(map(str, fingers))
#     return GESTURES.get(pattern, None)

# def perform_action(gesture):
#     global last_action_time
#     now = time.time()
#     if now - last_action_time < cooldown:
#         return
#     print(f"Gesture Detected: {gesture}")
#     if gesture == "PlayPause":
#         pyautogui.press("playpause")
#     elif gesture == "Next":
#         pyautogui.press("nexttrack")
#     elif gesture == "Previous":
#         pyautogui.press("prevtrack")
#     elif gesture == "VolumeUp":
#         pyautogui.press("volumeup")
#     elif gesture == "VolumeDown":
#         pyautogui.press("volumedown")
#     elif gesture == "Shuffle":
#         pyautogui.hotkey("ctrl", "s")
#     last_action_time = now

# cap = cv2.VideoCapture(0)
# print("Running Spotify Gesture Controller...")

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     frame = cv2.flip(frame, 1)
#     rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#     results = hands.process(rgb)

#     if results.multi_hand_landmarks:
#         for hand_landmarks in results.multi_hand_landmarks:
#             mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

#             fingers = detect_fingers(hand_landmarks.landmark)
#             gesture = recognize_gesture(fingers)

#             if gesture:
#                 perform_action(gesture)
#                 cv2.putText(frame, f'Gesture: {gesture}', (10, 40),
#                             cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

#     cv2.imshow("Spotify Gesture Control", frame)
#     if cv2.waitKey(1) & 0xFF == 27:  # ESC
#         break

# cap.release()
# cv2.destroyAllWindows()



# | Finger Pattern | Gesture Name | Action Performed           |
# | -------------- | ------------ | -------------------------- |
# | `11111`        | PlayPause    | ⏯ Toggle play/pause        |
# | `00000`        | Next         | ⏭ Next track               |
# | `11100`        | Previous     | ⏮ Previous track           |
# | `01100`        | VolumeUp     | 🔊 Increase volume         |
# | `10000`        | VolumeDown   | 🔉 Decrease volume         |
# | `11000`        | Shuffle      | 🔀 Toggle shuffle (Ctrl+S) |



# __________________________________________________________________________________________________________________________________

import tkinter as tk
from tkinter import messagebox
import subprocess
import threading
import os
import sys
import time
import cv2
import mediapipe as mp
import pyautogui
import shutil

# --- Gesture Logic Setup ---
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(static_image_mode=False,
                       max_num_hands=1,
                       min_detection_confidence=0.7,
                       min_tracking_confidence=0.7)

TIP_IDS = [4, 8, 12, 16, 20]

GESTURES = {
    "11111": "PlayPause",
    "00000": "Next",
    "11100": "Previous",
    "01100": "VolumeUp",
    "10000": "VolumeDown",
    "11000": "Shuffle"
}

cooldown = 1.5
last_action_time = 0
running = False

def detect_fingers(landmarks):
    fingers = []
    fingers.append(1 if landmarks[TIP_IDS[0]].x > landmarks[TIP_IDS[0] - 1].x else 0)
    for id in range(1, 5):
        fingers.append(1 if landmarks[TIP_IDS[id]].y < landmarks[TIP_IDS[id] - 2].y else 0)
    return fingers

def recognize_gesture(fingers):
    pattern = ''.join(map(str, fingers))
    return GESTURES.get(pattern, None)

def perform_action(gesture):
    global last_action_time
    now = time.time()
    if now - last_action_time < cooldown:
        return
    print(f"Gesture Detected: {gesture}")
    if gesture == "PlayPause":
        pyautogui.press("playpause")
    elif gesture == "Next":
        pyautogui.press("nexttrack")
    elif gesture == "Previous":
        pyautogui.press("prevtrack")
    elif gesture == "VolumeUp":
        pyautogui.press("volumeup")
    elif gesture == "VolumeDown":
        pyautogui.press("volumedown")
    elif gesture == "Shuffle":
        pyautogui.hotkey("ctrl", "s")
    last_action_time = now

def run_gesture_recognition():
    global running
    cap = cv2.VideoCapture(0)
    running = True
    while running:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                fingers = detect_fingers(hand_landmarks.landmark)
                gesture = recognize_gesture(fingers)
                if gesture:
                    perform_action(gesture)
                    cv2.putText(frame, f'Gesture: {gesture}', (10, 40),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

        cv2.imshow("Spotify Gesture Control", frame)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC key
            break
    cap.release()
    cv2.destroyAllWindows()

# --- GUI & Launch Logic ---
def launch_spotify():
    spotify_path = shutil.which("spotify")
    if spotify_path:
        subprocess.Popen([spotify_path], shell=True)
    else:
        subprocess.Popen("start spotify", shell=True)

gesture_thread = None

def start():
    global gesture_thread
    launch_spotify()
    gesture_thread = threading.Thread(target=run_gesture_recognition)
    gesture_thread.start()

def stop():
    global running
    running = False
    root.destroy()

root = tk.Tk()
root.title("Spotify Gesture Controller")
root.geometry("300x150")
root.resizable(False, False)

tk.Label(root, text="Control Spotify with hand gestures!", font=("Arial", 12)).pack(pady=10)

tk.Button(root, text="Start", command=start, bg="green", fg="white", width=15, height=2).pack(pady=5)
tk.Button(root, text="Exit", command=stop, bg="red", fg="white", width=15, height=2).pack(pady=5)

root.mainloop()
