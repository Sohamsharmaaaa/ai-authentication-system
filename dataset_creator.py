import cv2
import os

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

print("📸 Press 's' to capture image")
print("❌ Press 'q' to quit")

count = 0

while True:

    ret, frame = cap.read()

    if not ret:
        continue

    # Show camera
    cv2.imshow("Dataset Creator", frame)

    key = cv2.waitKey(1)

    # Press 's' to save image
    if key == ord('s'):
        filename = os.path.join(dataset_path, f"{count}.jpg")
        cv2.imwrite(filename, frame)
        print(f"✅ Image saved: {filename}")
        count += 1

    # Press 'q' to quit
    elif key == ord('q'):
        break

# -------------------------------
# Cleanup
# -------------------------------

cap.release()
cv2.destroyAllWindows()

print(f"\n🎉 Dataset created with {count} images!")