import sqlite3
from utils.security import hash_password, verify_password

DATABASE = "database/medilink.db"


# ==========================
# DATABASE CONNECTION
# ==========================

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

# ==========================
# CREATE DATABASE
# ==========================

def create_database():

    conn = get_connection()
    cursor = conn.cursor()

    # ==========================
    # USERS TABLE
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        full_name TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        phone TEXT,

        age INTEGER,

        gender TEXT,

        password TEXT NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    # ==========================
    # MEDICATION REMINDERS
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reminders(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER NOT NULL,

        medication TEXT NOT NULL,

        dosage TEXT NOT NULL,

        reminder_time TEXT NOT NULL,

        FOREIGN KEY(user_id)
        REFERENCES users(id)

    )
    """)

    # ==========================
    # AI HISTORY
    # ==========================

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ai_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER NOT NULL,

        symptoms TEXT NOT NULL,

        ai_response TEXT NOT NULL,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

        FOREIGN KEY(user_id)
        REFERENCES users(id)

    )
    """)

    conn.commit()
    conn.close()


# ==========================
# REGISTER USER
# ==========================

def register_user(
    full_name,
    email,
    phone,
    age,
    gender,
    password
):

    full_name = full_name.strip()
    email = email.strip().lower()
    phone = phone.strip()

    conn = get_connection()
    cursor = conn.cursor()

    hashed_password = hash_password(password)
    try:

        cursor.execute("""

        INSERT INTO users(

            full_name,
            email,
            phone,
            age,
            gender,
            password

        )

        VALUES(?,?,?,?,?,?)

        """, (

            full_name,
            email,
            phone,
            age,
            gender,
            hashed_password

        ))

        conn.commit()

        return True

    except sqlite3.IntegrityError:

        return False

    finally:

        conn.close()


# ==========================
# LOGIN USER
# ==========================

def login_user(email, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE LOWER(email)=LOWER(?)
        """,
        (email.strip(),)
    )

    user = cursor.fetchone()

    conn.close()

    if user and verify_password(password, user[6]):
        return user

    return None


# ==========================
# ADD REMINDER
# ==========================

def add_reminder(
    user_id,
    medication,
    dosage,
    reminder_time
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO reminders(

        user_id,
        medication,
        dosage,
        reminder_time

    )

    VALUES(?,?,?,?)

    """, (

        user_id,
        medication,
        dosage,
        reminder_time

    ))

    conn.commit()
    conn.close()


# ==========================
# GET REMINDERS
# ==========================

def get_reminders(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT *

    FROM reminders

    WHERE user_id=?

    ORDER BY reminder_time

    """, (user_id,))

    reminders = cursor.fetchall()

    conn.close()

    return reminders


# ==========================
# TOTAL REMINDERS
# ==========================

def get_total_reminders(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT COUNT(*)

    FROM reminders

    WHERE user_id=?

    """, (user_id,))

    total = cursor.fetchone()[0]

    conn.close()

    return total

# ==========================
# DELETE REMINDER
# ==========================

def delete_reminder(reminder_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM reminders
        WHERE id=?
        """,
        (reminder_id,)
    )

    conn.commit()
    conn.close()


# ==========================
# USER PROFILE
# ==========================

def get_user_profile(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT

        full_name,
        email,
        phone,
        age,
        gender,
        created_at

    FROM users

    WHERE id=?

    """, (user_id,))

    user = cursor.fetchone()

    conn.close()

    return user

# ==========================
# UPDATE USER PROFILE
# ==========================

def update_user_profile(
    user_id,
    full_name,
    phone,
    age,
    gender
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE users
        SET
            full_name=?,
            phone=?,
            age=?,
            gender=?
        WHERE id=?
        """,
        (
            full_name,
            phone,
            age,
            gender,
            user_id
        )
    )

    conn.commit()
    conn.close()


# ==========================
# TOTAL USERS
# ==========================

def get_total_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT COUNT(*)

    FROM users

    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total


# ==========================
# SAVE AI HISTORY
# ==========================

def save_ai_history(
    user_id,
    symptoms,
    ai_response
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    INSERT INTO ai_history(

        user_id,
        symptoms,
        ai_response

    )

    VALUES(?,?,?)

    """, (

        user_id,
        symptoms,
        ai_response

    ))

    conn.commit()
    conn.close()


# ==========================
# GET AI HISTORY
# ==========================

def get_ai_history(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT

        symptoms,
        ai_response,
        created_at

    FROM ai_history

    WHERE user_id=?

    ORDER BY created_at DESC

    """, (user_id,))

    history = cursor.fetchall()

    conn.close()

    return history


# ==========================
# TOTAL AI CHECKS
# ==========================

def get_total_ai_checks(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""

    SELECT COUNT(*)

    FROM ai_history

    WHERE user_id=?

    """, (user_id,))

    total = cursor.fetchone()[0]

    conn.close()

    return total