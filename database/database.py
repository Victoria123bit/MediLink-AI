import sqlite3
import bcrypt
import random
import secrets

from datetime import datetime, timedelta


# ==========================================
# DATABASE CONNECTION
# ==========================================

DATABASE_NAME = "database/medilink.db"


def get_connection():

    conn = sqlite3.connect(DATABASE_NAME)

    conn.row_factory = sqlite3.Row

    return conn


# ==========================================
# HASH PASSWORD
# ==========================================

def hash_password(password):

    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()


# ==========================================
# VERIFY PASSWORD
# ==========================================

def verify_password(password, hashed):

    return bcrypt.checkpw(
        password.encode(),
        hashed.encode()
    )


# ==========================================
# CREATE DATABASE
# ==========================================

def create_database():

    conn = get_connection()

    cursor = conn.cursor()

    # ======================================
    # USERS TABLE
    # ======================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        full_name TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL,

        phone TEXT,

        age INTEGER,

        gender TEXT,

        created_at TEXT

    )

    """)

    # ======================================
    # MEDICATION REMINDERS
    # ======================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS reminders(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        medication TEXT,

        dosage TEXT,

        reminder_time TEXT,

        created_at TEXT

    )

    """)

    # ======================================
    # AI HISTORY
    # ======================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS ai_history(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        user_id INTEGER,

        symptoms TEXT,

        response TEXT,

        created_at TEXT

    )

    """)

    # ======================================
    # PASSWORD RESET OTP
    # ======================================

    cursor.execute("""

    CREATE TABLE IF NOT EXISTS password_reset_otp(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        email TEXT,

        otp TEXT,

        expires_at TEXT

    )

    """)

    conn.commit()

    conn.close()

# ==========================================
# CREATE USER
# ==========================================

def create_user(
    full_name,
    email,
    password,
    phone,
    age,
    gender
):

    conn = get_connection()
    cursor = conn.cursor()

    hashed_password = hash_password(password)

    cursor.execute(
        """
        INSERT INTO users(
            full_name,
            email,
            password,
            phone,
            age,
            gender,
            created_at
        )
        VALUES(?,?,?,?,?,?,?)
        """,
        (
            full_name,
            email.lower(),
            hashed_password,
            phone,
            age,
            gender,
            datetime.now().isoformat()
        )
    )

    conn.commit()
    conn.close()
# ==========================================
# REGISTER USER
# ==========================================

def register_user(
    full_name,
    email,
    password,
    phone,
    age,
    gender
):

    if email_exists(email):
        return False

    create_user(
        full_name,
        email,
        password,
        phone,
        age,
        gender
    )

    return True

# ==========================================
# EMAIL EXISTS
# ==========================================

def email_exists(email):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT id
        FROM users
        WHERE LOWER(email)=LOWER(?)
        """,
        (email.lower(),)
    )

    exists = cursor.fetchone() is not None

    conn.close()

    return exists


# ==========================================
# LOGIN USER
# ==========================================

def login_user(email, password):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE LOWER(email)=LOWER(?)
        """,
        (email.lower(),)
    )

    user = cursor.fetchone()

    conn.close()

    if user and verify_password(password, user["password"]):
        return user

    return None


# ==========================================
# GET USER PROFILE
# ==========================================

def get_user_profile(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            full_name,
            email,
            phone,
            age,
            gender,
            created_at
        FROM users
        WHERE id=?
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    conn.close()

    return user


# ==========================================
# TOTAL USERS
# ==========================================

def get_total_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) AS total FROM users"
    )

    total = cursor.fetchone()["total"]

    conn.close()

    return total


# ==========================================
# UPDATE PASSWORD
# ==========================================

def update_password(email, new_password):

    conn = get_connection()
    cursor = conn.cursor()

    hashed_password = hash_password(new_password)

    cursor.execute(
        """
        UPDATE users
        SET password=?
        WHERE LOWER(email)=LOWER(?)
        """,
        (
            hashed_password,
            email.lower()
        )
    )

    conn.commit()
    conn.close()

# ==========================================
# ADD REMINDER
# ==========================================

def add_reminder(
    user_id,
    medication,
    dosage,
    reminder_time
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO reminders(
            user_id,
            medication,
            dosage,
            reminder_time,
            created_at
        )
        VALUES(?,?,?,?,?)
        """,
        (
            user_id,
            medication,
            dosage,
            reminder_time,
            datetime.now().isoformat()
        )
    )

    conn.commit()
    conn.close()


# ==========================================
# GET REMINDERS
# ==========================================

def get_reminders(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM reminders
        WHERE user_id=?
        ORDER BY reminder_time
        """,
        (user_id,)
    )

    reminders = cursor.fetchall()

    conn.close()

    return reminders


# ==========================================
# TOTAL REMINDERS
# ==========================================

def get_total_reminders(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*) AS total
        FROM reminders
        WHERE user_id=?
        """,
        (user_id,)
    )

    total = cursor.fetchone()["total"]

    conn.close()

    return total

# ==========================================
# SAVE AI HISTORY
# ==========================================

def save_ai_history(
    user_id,
    symptoms,
    response
):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO ai_history(
            user_id,
            symptoms,
            response,
            created_at
        )
        VALUES(?,?,?,?)
        """,
        (
            user_id,
            symptoms,
            response,
            datetime.now().isoformat()
        )
    )

    conn.commit()
    conn.close()


# ==========================================
# GET AI HISTORY
# ==========================================

def get_ai_history(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM ai_history
        WHERE user_id=?
        ORDER BY created_at DESC
        """,
        (user_id,)
    )

    history = cursor.fetchall()

    conn.close()

    return history


# ==========================================
# TOTAL AI CHECKS
# ==========================================

def get_total_ai_checks(user_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT COUNT(*) AS total
        FROM ai_history
        WHERE user_id=?
        """,
        (user_id,)
    )

    total = cursor.fetchone()["total"]

    conn.close()

    return total


# ==========================================
# CREATE PASSWORD RESET OTP
# ==========================================

def create_password_reset_otp(email):

    conn = get_connection()
    cursor = conn.cursor()

    otp = str(random.randint(100000, 999999))

    expiry = (
        datetime.now() +
        timedelta(minutes=10)
    ).isoformat()

    cursor.execute(
        """
        DELETE FROM password_reset_otp
        WHERE LOWER(email)=LOWER(?)
        """,
        (email.lower(),)
    )

    cursor.execute(
        """
        INSERT INTO password_reset_otp(
            email,
            otp,
            expires_at
        )
        VALUES(?,?,?)
        """,
        (
            email.lower(),
            otp,
            expiry
        )
    )

    conn.commit()
    conn.close()

    return otp


# ==========================================
# VERIFY PASSWORD RESET OTP
# ==========================================

def verify_password_reset_otp(email, otp):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT otp, expires_at
        FROM password_reset_otp
        WHERE LOWER(email)=LOWER(?)
        """,
        (email.lower(),)
    )

    row = cursor.fetchone()

    conn.close()

    if row is None:
        return False

    if row["otp"] != otp:
        return False

    expiry = datetime.fromisoformat(
        row["expires_at"]
    )

    if datetime.now() > expiry:
        return False

    return True


# ==========================================
# DELETE PASSWORD RESET OTP
# ==========================================

def delete_password_reset_otp(email):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM password_reset_otp
        WHERE LOWER(email)=LOWER(?)
        """,
        (email.lower(),)
    )

    conn.commit()
    conn.close()