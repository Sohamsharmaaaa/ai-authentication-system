import tkinter as tk
import cv2
import face_recognition
import datetime
import os
import keyboard
import time
import speech_recognition as sr
import pyttsx3
import threading
import sys

# -------------------------------
# Path Fix
# -------------------------------

def get_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

# -------------------------------
# Directories
# -------------------------------

BASE_DIR = os.getcwd()
INTRUDER_DIR = os.path.join(BASE_DIR, "intruders")
LOG_DIR = os.path.join(BASE_DIR, "logs")

os.makedirs(INTRUDER_DIR, exist_ok=True)
os.makedirs(LOG_DIR, exist_ok=True)

# -------------------------------
# Voice Engine
# -------------------------------

engine = pyttsx3.init()
engine.setProperty('rate', 170)

def speak(text):
    def run():
        engine.say(text)
        engine.runAndWait()
    threading.Thread(target=run, daemon=True).start()

# -------------------------------
# Global Flags
# -------------------------------

voice_running = False
last_capture_time = 0

# -------------------------------
# Load Dataset (FAST)
# -------------------------------

dataset_base = get_path("dataset")

known_faces = []

if not os.path.exists(dataset_base) or not os.listdir(dataset_base):
    print("❌ No dataset found. Run dataset_creator.py first.")
    exit()

print("⏳ Loading dataset...")

for user in os.listdir(dataset_base):

    user_path = os.path.join(dataset_base, user)

    if not os.path.isdir(user_path):
        continue

    for file in os.listdir(user_path):

        img_path = os.path.join(user_path, file)

        try:
            img = face_recognition.load_image_file(img_path)
            enc = face_recognition.face_encodings(img)

            if enc:
                known_faces.append(enc[0])

        except:
            continue

print(f"✅ Loaded {len(known_faces)} face encodings")

# -------------------------------
# Webcam
# -------------------------------

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera error")
    exit()

# -------------------------------
# Unlock
# -------------------------------

def unlock():
    cap.release()
    root.quit()
    root.destroy()

# -------------------------------
# Voice Override (IMPROVED)
# -------------------------------

def voice_override():

    global voice_running

    if voice_running:
        return

    voice_running = True

    def listen():
        global voice_running

        recognizer = sr.Recognizer()
        recognizer.energy_threshold = 300
        recognizer.pause_threshold = 0.8

        try:
            speak("Intruder detected. Say the secret code")

            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=1)

                audio = recognizer.listen(source, timeout=5)
                command = recognizer.recognize_google(audio).lower()

                print("Voice:", command)

                if "i am pikachu" in command:
                    speak("Thank you. Access granted")
                    unlock()
                else:
                    speak("Access denied")

        except:
            speak("Voice not recognized")

        voice_running = False

    threading.Thread(target=listen, daemon=True).start()

# -------------------------------
# Intruder Capture
# -------------------------------

def capture_intruder(frame):

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(INTRUDER_DIR, f"intruder_{timestamp}.jpg")

    cv2.imwrite(filename, frame)
    log_intruder(timestamp)

# -------------------------------
# Logging
# -------------------------------

def log_intruder(timestamp):

    log_file = os.path.join(LOG_DIR, "security_log.txt")

    with open(log_file, "a") as f:
        f.write(f"[{timestamp}] Unknown face detected\n")

# -------------------------------
# Face Scan (FAST + SMOOTH)
# -------------------------------

def scan_face():

    global last_capture_time

    while True:

        ret, frame = cap.read()
        if not ret:
            continue

        # 🔥 SPEED OPTIMIZATION (resize)
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        rgb = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        faces = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, faces)

        for encoding in encodings:

            matches = face_recognition.compare_faces(known_faces, encoding, tolerance=0.5)

            if True in matches:
                unlock()
                return

        # Intruder logic
        if len(encodings) > 0:

            if time.time() - last_capture_time > 15:
                capture_intruder(frame)
                last_capture_time = time.time()
                voice_override()

        time.sleep(0.2)

# -------------------------------
# Keyboard Protection
# -------------------------------

def reinforce_keyboard_block():
    keyboard.block_key("windows")
    keyboard.block_key("alt")
    keyboard.block_key("tab")
    keyboard.block_key("esc")
    keyboard.block_key("shift")
    root.after(1000, reinforce_keyboard_block)

keyboard.add_hotkey("alt+tab", lambda: None, suppress=True)
keyboard.add_hotkey("alt+f4", lambda: None, suppress=True)
keyboard.add_hotkey("ctrl+esc", lambda: None, suppress=True)

# -------------------------------
# UI
# -------------------------------

root = tk.Tk()
root.attributes('-fullscreen', True)
root.configure(bg="black")
root.protocol("WM_DELETE_WINDOW", lambda: None)

# Always on top
def keep_on_top():
    root.attributes('-topmost', True)
    root.lift()
    root.focus_force()
    root.after(1000, keep_on_top)

keep_on_top()
reinforce_keyboard_block()

label = tk.Label(
    root,
    text="AI Security System\nScanning Face...",
    fg="white",
    bg="black",
    font=("Arial", 40)
)

label.pack(expand=True)

# -------------------------------
# Start Thread
# -------------------------------

threading.Thread(target=scan_face, daemon=True).start()

root.mainloop()