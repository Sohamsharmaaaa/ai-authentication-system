import cv2
import os
import time

# -------------------------------
# Get User Name
# -------------------------------

user_name = input("Enter your name: ").strip().lower()

if not user_name:
    print("❌ Name cannot be empty")
    exit()

# -------------------------------
# Create Dataset Folder
# -------------------------------

dataset_path = os.path.join("dataset", user_name)
os.makedirs(dataset_path, exist_ok=True)

print(f"📁 Dataset will be saved in: {dataset_path}")

# -------------------------------
# Start Camera
# -------------------------------

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera not accessible")
    exit()

print("📸 Capturing images automatically...")

count = 0
max_images = 30   # 🔥 you can increase

# -------------------------------
# Capture Loop
# -------------------------------

while count < max_images:

    ret, frame = cap.read()

    if not ret:
        continue

    # Save image
    filename = os.path.join(dataset_path, f"{count}.jpg")
    cv2.imwrite(filename, frame)

    print(f"✅ Captured: {filename}")

    count += 1

    # Show camera (optional)
    cv2.imshow("Dataset Creator", frame)

    # Small delay (important)
    time.sleep(0.3)

    # Exit if window closed (optional safety)
    if cv2.waitKey(1) == 27:
        break

# -------------------------------
# Cleanup
# -------------------------------

cap.release()
cv2.destroyAllWindows()

print(f"\n🎉 Dataset created with {count} images!")