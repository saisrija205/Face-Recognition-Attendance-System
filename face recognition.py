import cv2
from database import get_student
from attendance import mark_attendance

# ===============================
# Load Face Detector
# ===============================

face_cascade = cv2.CascadeClassifier(
    "haarcascade/haarcascade_frontalface_default.xml"
)

if face_cascade.empty():
    print("Error: Haar Cascade file not found!")
    exit()

# ===============================
# Load Trained Model
# ===============================

recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read("trainer/trainer.yml")

# ===============================
# Start Camera
# ===============================

cam = cv2.VideoCapture(0)

if not cam.isOpened():
    print("Unable to open webcam.")
    exit()

print("Face Recognition Started")
print("Press Q to Quit")

# ===============================
# Recognition Loop
# ===============================

while True:

    ret, frame = cam.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(100, 100)
    )

    for (x, y, w, h) in faces:

        student_id, confidence = recognizer.predict(gray[y:y+h, x:x+w])

        if confidence < 60:

            student = get_student(student_id)

            if student:

                name = student[1]

                # Save attendance
                mark_attendance(student_id, name)

                text = f"{name}"

                color = (0, 255, 0)

            else:

                text = "Unknown"

                color = (0, 0, 255)

        else:

            text = "Unknown"

            color = (0, 0, 255)

        cv2.rectangle(frame,
                      (x, y),
                      (x+w, y+h),
                      color,
                      2)

        cv2.putText(frame,
                    text,
                    (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    color,
                    2)

    cv2.imshow("Face Recognition Attendance", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()

cv2.destroyAllWindows()

print("Program Closed.")