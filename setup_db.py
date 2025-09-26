import sqlite3

# Create one database
conn = sqlite3.connect("college.db")
cursor = conn.cursor()

# ---------- USERS TABLE ----------
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")

# Insert sample users
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ("admin", "1234"))
cursor.execute("INSERT OR IGNORE INTO users (username, password) VALUES (?, ?)", ("user1", "pass1"))


# ---------- STUDENTS TABLE ----------
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    admission_no TEXT,
    first_name TEXT,
    last_name TEXT,
    father_name TEXT,
    dob_day TEXT,
    dob_month TEXT,
    dob_year TEXT,
    mobile_no TEXT,
    alt_phone_no TEXT,
    email TEXT,
    aadhar_no TEXT,
    gender TEXT,
    religion TEXT,
    blood_group TEXT,
    community TEXT,
    department TEXT,
    course TEXT,
    year_of_study TEXT,
    country TEXT,
    city TEXT,
    quota TEXT,
    address TEXT
)
""")

# Commit and close
conn.commit()
conn.close()
print("✅ Database (college.db) with users & students tables created successfully!")

