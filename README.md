# AI-Based System Security Project

Developed by Soham Sharma

## Overview

This project is an AI-based system security application that enhances workstation protection using face recognition and voice authentication. It acts as an additional security layer that restricts unauthorized access and monitors intrusion attempts in real time.

The system uses computer vision and speech recognition to verify user identity. If an unauthorized person attempts access, the system captures their image, logs the event, and requests a secret voice command for override.

---

## Features

* Real-time face recognition authentication
* Voice-based access control using a secret phrase
* Intruder detection with image capture
* Automatic logging of unauthorized access attempts
* Fullscreen lock interface
* Basic keyboard shortcut blocking
* Dynamic dataset creation for multiple users

---

## Technologies Used

* Python
* OpenCV
* face_recognition
* SpeechRecognition
* pyttsx3
* Tkinter

---

## Project Structure

```
ai-authentication-system/
│
├── dataset/              # Stores user face data  
├── intruders/            # Stores captured intruder images  
├── logs/                 # Stores security logs  
│
├── dataset_creator.py    # Script to create user dataset  
├── security_lock.py      # Main security system  
├── requirements.txt      # Dependencies  
```

---

## Installation and Setup

### Step 1: Clone the repository

```bash
git clone https://github.com/Sohamsharmaaaa/ai-authentication-system.git
cd ai-authentication-system
```

### Step 2: Install required dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Create your face dataset

Run the dataset creator script:

```bash
python dataset_creator.py
```

Enter your name when prompted.
Press 'S' to capture images and 'Q' to finish.

Your dataset will be saved in:

```
dataset/your_name/
```

For better accuracy, capture 15–20 images with different angles and lighting conditions.

### Step 4: Run the security system

```bash
python security_lock.py
```

---

## How the System Works

1. The system starts and locks the screen

2. The camera continuously scans for faces

3. If an authorized face is detected, access is granted

4. If an unknown face is detected:

   * The image is captured and saved
   * The event is logged
   * The system asks for voice authentication

5. The user must say the secret phrase:

```
I am pikachu
```

If the phrase matches, access is granted.

---

## Output

* Intruder images are stored in the "intruders" folder
* Logs are stored in "logs/security_log.txt"

---

## Security Limitations

This is an application-level security system and does not provide full operating system-level protection.

Known limitations:

* Cannot block Ctrl + Alt + Delete
* Cannot prevent Task Manager access
* Can be bypassed using virtual desktops
* Vulnerable to photo-based spoofing
* Voice authentication can be bypassed using recordings

---

## Future Improvements

* Liveness detection to prevent photo spoofing
* Email or mobile alerts for intruder detection
* Intruder video recording
* Multi-user authentication system
* Deeper integration with operating system security

---

## About the Project

This project demonstrates practical implementation of AI in system security. It combines computer vision, voice processing, and real-time monitoring to simulate a smart authentication system.

It is designed as a learning and portfolio project to showcase applied knowledge in cybersecurity and artificial intelligence.

---

## Author

Soham Sharma

---

## Disclaimer

This project is intended for educational purposes only and should not be used as a replacement for real operating system security mechanisms.
