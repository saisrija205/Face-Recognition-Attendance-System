import sqlite3
import os

# ==========================
# Create Database Folder
# ==========================

if not os.path.exists("database"):
    os.makedirs("database")

DB_PATH = "database/attendance.db"


# ==========================
# Connect Database
# ==========================

def connect_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Student Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        department TEXT,
        year TEXT
    )
    """)

    # Attendance Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attendance(
        id INTEGER,
        name TEXT,
        date TEXT,
        time TEXT
    )
    """)

    conn.commit()
    return conn


# ==========================
# Add Student
# ==========================

def add_student(student_id, name, department, year):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students(id,name,department,year)
    VALUES(?,?,?,?)
    """, (student_id, name, department, year))

    conn.commit()
    conn.close()

    print("Student Added Successfully.")


# ==========================
# Get Student
# ==========================

def get_student(student_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM students
    WHERE id=?
    """, (student_id,))

    student = cursor.fetchone()

    conn.close()

    return student


# ==========================
# Show All Students
# ==========================

def show_students():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    conn.close()

    if len(students) == 0:
        print("\nNo Students Found\n")
        return

    print("\n---------- Student List ----------")

    for s in students:
        print(f"ID : {s[0]}")
        print(f"Name : {s[1]}")
        print(f"Department : {s[2]}")
        print(f"Year : {s[3]}")
        print("----------------------------")


# ==========================
# Delete Student
# ==========================

def delete_student(student_id):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    DELETE FROM students
    WHERE id=?
    """, (student_id,))

    conn.commit()
    conn.close()

    print("Student Deleted Successfully.")


# ==========================
# Mark Attendance
# ==========================

def mark_attendance(student_id, name, date, time):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO attendance
    VALUES(?,?,?,?)
    """, (student_id, name, date, time))

    conn.commit()
    conn.close()


# ==========================
# Show Attendance
# ==========================

def show_attendance():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM attendance")

    records = cursor.fetchall()

    conn.close()

    if len(records) == 0:
        print("\nAttendance Not Found\n")
        return

    print("\n========== Attendance ==========")

    for r in records:

        print(f"ID : {r[0]}")
        print(f"Name : {r[1]}")
        print(f"Date : {r[2]}")
        print(f"Time : {r[3]}")
        print("--------------------------")


# ==========================
# Database Initialization
# ==========================

connect_db()

print("Database Ready.")