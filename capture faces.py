import cv2
import os
from database import get_student

# ==========================
# Create Dataset Folder
# ==========================

if not os.path.exists("dataset"):
    os.makedirs("dataset")

# ==========================
# Load Haar Cascade
# ==========================

cascade_path = "haarcascade/haarcascade_frontalface_default.xml"

face_detector = cv2.CascadeClassifier(cascade_path)

if face_detector.empty():
    print("Error: Haar Cascade file not found!")
    exit()

# ==========================
# Get Student ID
# ==========================

student_id = input("Enter Student ID: ")

student = get_student(int(student_id))

if student is None:
    print("Student ID not found in database.")
    print("Please register the student first.")
    exit()

print("\nStudent Found")
print("ID :", student[0])
print("Name :", student[1])

# ==========================
# Start Camera
# ==========================

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Unable to access webcam.")
    exit()

print("\nCapturing face images...")
print("Look at the camera.")
print("Press 'q' to quit.")

count = 0

# ==========================
# Capture Images
# ==========================

while True:

    ret, img = cam.read()

    if not ret:
        print("Failed to capture image.")
        break

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(100, 100)
    )

    for (x, y, w, h) in faces:

        count += 1

        face = gray[y:y+h, x:x+w]

        filename = f"dataset/User.{student_id}.{count}.jpg"

        cv2.imwrite(filename, face)

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        cv2.putText(
            img,
            f"Image {count}/50",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 0, 0),
            2
        )

    cv2.imshow("Face Capture", img)

    key = cv2.waitKey(100)

    if key == ord('q'):
        break

    if count >= 50:
        break

# ==========================
# Finish
# ==========================

cam.release()
cv2.destroyAllWindows()

print("\nFace Capture Completed!")
print(f"{count} images saved in dataset folder.")