from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

DB_NAME = "college.db"   # one DB for both users & students

# ---------- USER LOGIN ----------
def check_user(username, password):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = cursor.fetchone()
    conn.close()
    return result

@app.route("/")
def login_page():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if check_user(username, password):
        return redirect(url_for("registration_form"))
    else:
        return render_template("login.html", error="Invalid username or password!")

# ---------- STUDENT REGISTRATION ----------
@app.route("/forms1")
def registration_form():
    return render_template("forms1.html")  # your student registration form

@app.route("/register", methods=["POST"])
def register():
    data = request.form
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO students (
        admission_no, first_name, last_name, father_name,
        dob_day, dob_month, dob_year,
        mobile_no, alt_phone_no, email, aadhar_no,
        gender, religion, blood_group, community, department,
        course, year_of_study, country, city, quota, address
    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        data.get("admission_no"),
        data.get("first_name"),
        data.get("last_name"),
        data.get("father_name"),
        data.get("day"),
        data.get("month"),
        data.get("year"),
        data.get("mobile_no"),
        data.get("alt_phone_no"),
        data.get("email"),
        data.get("aadhar_no"),
        data.get("gender"),
        data.get("religion"),
        data.get("blood_group"),
        data.get("community"),
        data.get("department"),
        data.get("course"),
        data.get("year_of_study"),
        data.get("country"),
        data.get("city"),
        data.get("quota"),
        data.get("address")
    ))

    conn.commit()
    conn.close()

    return redirect(url_for("success"))

# ---------- SUCCESS PAGE ----------
@app.route("/success")
def success():
    return render_template("success.html")


if __name__ == "__main__":
    app.run(debug=True)
# Note: Ensure you have run setup_db.py to create the database and tables before starting the app.
