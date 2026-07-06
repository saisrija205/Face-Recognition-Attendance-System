import cv2
import numpy as np
from PIL import Image
import os

# ==========================
# Create Trainer Folder
# ==========================

if not os.path.exists("trainer"):
    os.makedirs("trainer")

# ==========================
# Create Recognizer
# ==========================

recognizer = cv2.face.LBPHFaceRecognizer_create()

# ==========================
# Dataset Path
# ==========================

dataset_path = "dataset"

# ==========================
# Function to Read Images
# ==========================

def get_images_and_labels(path):

    image_paths = [
        os.path.join(path, f)
        for f in os.listdir(path)
        if f.endswith(".jpg")
    ]

    face_samples = []
    ids = []

    for image_path in image_paths:

        # Convert image to grayscale
        img = Image.open(image_path).convert('L')

        img_numpy = np.array(img, 'uint8')

        # Filename format:
        # User.ID.Count.jpg
        filename = os.path.basename(image_path)

        student_id = int(filename.split(".")[1])

        face_samples.append(img_numpy)
        ids.append(student_id)

    return face_samples, ids


# ==========================
# Check Dataset
# ==========================

if not os.path.exists(dataset_path):
    print("Dataset folder not found.")
    exit()

if len(os.listdir(dataset_path)) == 0:
    print("No images found in dataset.")
    print("Capture student faces first.")
    exit()

print("Reading images...")

faces, ids = get_images_and_labels(dataset_path)

print("Training model...")

recognizer.train(faces, np.array(ids))

recognizer.save("trainer/trainer.yml")

print("\n================================")
print("Training Completed Successfully")
print("Model saved as:")
print("trainer/trainer.yml")
print("================================")