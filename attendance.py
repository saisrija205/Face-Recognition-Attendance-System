import csv
import os
from datetime import datetime
from database import connect_db

# ==========================
# Create Attendance Folder
# ==========================

if not os.path.exists("attendance"):
    os.makedirs("attendance")

CSV_FILE = "attendance/attendance.csv"

# ==========================
# Create CSV File
# ==========================

if not os.path.exists(CSV_FILE):

    with open(CSV_FILE, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Student ID",
                         "Name",
                         "Date",
                         "Time"])


# ==========================
# Mark Attendance
# ==========================

def mark_attendance(student_id, name):

    today = datetime.now().strftime("%d-%m-%Y")
    current_time = datetime.now().strftime("%H:%M:%S")

    # ==========================
    # Prevent Duplicate Entries
    # ==========================

    already_marked = False

    with open(CSV_FILE, "r") as file:

        reader = csv.reader(file)

        next(reader)

        for row in reader:

            if len(row) > 0:

                if row[0] == str(student_id) and row[2] == today:

                    already_marked = True
                    break

    if already_marked:

        return

    # ==========================
    # Save to CSV
    # ==========================

    with open(CSV_FILE, "a", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            student_id,
            name,
            today,
            current_time
        ])

    # ==========================
    # Save to Database
    # ==========================

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO attendance
        VALUES(?,?,?,?)
    """, (
        student_id,
        name,
        today,
        current_time
    ))

    conn.commit()

    conn.close()

    print(f"{name} Attendance Marked")


# ==========================
# View Attendance
# ==========================

def show_attendance():

    if not os.path.exists(CSV_FILE):

        print("Attendance File Not Found")

        return

    with open(CSV_FILE, "r") as file:

        reader = csv.reader(file)

        print("\n========== Attendance ==========\n")

        for row in reader:

            print(row)


# ==========================
# Test
# ==========================

if __name__ == "__main__":

    show_attendance()