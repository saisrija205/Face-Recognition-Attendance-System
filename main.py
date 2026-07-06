import os

# Create required folders automatically
folders = [
    "dataset",
    "trainer",
    "attendance",
    "database",
    "haarcascade",
    "images"
]

for folder in folders:
    if not os.path.exists(folder):
        os.makedirs(folder)


def register_student():
    print("\n===================================")
    print(" Student Registration")
    print("===================================")
    print("This feature will be added after database.py is completed.\n")


def capture_faces():
    print("\n===================================")
    print(" Capture Student Faces")
    print("===================================")
    print("This feature will be added after capture_faces.py is completed.\n")


def train_model():
    print("\n===================================")
    print(" Train Face Recognition Model")
    print("===================================")
    print("This feature will be added after train_model.py is completed.\n")


def recognize_face():
    print("\n===================================")
    print(" Face Recognition Attendance")
    print("===================================")
    print("This feature will be added after face_recognition.py is completed.\n")


def view_attendance():
    print("\n===================================")
    print(" Attendance Report")
    print("===================================")
    print("This feature will be added after attendance.py is completed.\n")


while True:

    print("\n")
    print("==============================================")
    print(" FACE RECOGNITION ATTENDANCE SYSTEM")
    print("==============================================")
    print("1. Register Student")
    print("2. Capture Face")
    print("3. Train Model")
    print("4. Start Face Recognition")
    print("5. View Attendance")
    print("6. Exit")
    print("==============================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        register_student()

    elif choice == "2":
        capture_faces()

    elif choice == "3":
        train_model()

    elif choice == "4":
        recognize_face()

    elif choice == "5":
        view_attendance()

    elif choice == "6":
        print("\nThank you for using the Face Recognition Attendance System.")
        break

    else:
        print("\nInvalid choice! Please try again.")