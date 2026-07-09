import os
import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv


# ==========================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================

load_dotenv()

SMTP_EMAIL = st.secrets.get("SMTP_EMAIL", os.getenv("SMTP_EMAIL"))
SMTP_PASSWORD = st.secrets.get("SMTP_PASSWORD", os.getenv("SMTP_PASSWORD"))
SMTP_SERVER = st.secrets.get("SMTP_SERVER", os.getenv("SMTP_SERVER", "smtp.gmail.com"))
SMTP_PORT = int(st.secrets.get("SMTP_PORT", os.getenv("SMTP_PORT", 587)))

print("SMTP EMAIL:", SMTP_EMAIL)

if SMTP_PASSWORD:
    print("SMTP PASSWORD: Loaded Successfully")
else:
    print("SMTP PASSWORD: Not Found")



# ==========================================
# SEND EMAIL
# ==========================================

def send_email(
    recipient_email,
    subject,
    html_message,
    plain_message=None
):
    """
    Sends an email using Gmail SMTP.

    Returns:
        True  -> Email sent successfully
        False -> Failed to send email
    """

    try:

        message = EmailMessage()

        message["From"] = SMTP_EMAIL
        message["To"] = recipient_email
        message["Subject"] = subject

        if plain_message is None:
            plain_message = "Please view this email in an HTML-compatible email client."

        message.set_content(plain_message)
        message.add_alternative(html_message, subtype="html")

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:

            server.starttls()

            server.login(
                SMTP_EMAIL,
                SMTP_PASSWORD
            )

            server.send_message(message)

        return True

    except Exception as e:

        print(f"Email Error: {e}")

        return False


# ==========================================
# PASSWORD RESET EMAIL
# ==========================================

def send_password_reset_email(
    recipient_email,
    reset_link
):

    subject = "Reset Your MediLink AI Password"

    html = f"""
    <html>
    <body style="font-family:Arial,sans-serif;">

        <h2 style="color:#1565C0;">
            MediLink AI
        </h2>

        <p>Hello,</p>

        <p>
        We received a request to reset your password.
        </p>

        <p>
        Click the button below to create a new password.
        </p>

        <p>

        <a href="{reset_link}" target="_blank"
        style="
            background:#1565C0;
            color:white;
            padding:12px 20px;
            text-decoration:none;
            border-radius:6px;
            display:inline-block;
        ">

        Reset Password

        </a>

        </p>

        <p>
        If you didn't request this password reset,
        you can safely ignore this email.
        </p>

        <hr>

        <p style="color:gray;font-size:12px;">
        © 2026 MediLink AI
        </p>

    </body>
    </html>
    """

    return send_email(
        recipient_email,
        subject,
        html
    )


# ==========================================
# EMAIL VERIFICATION
# ==========================================

def send_verification_email(
    recipient_email,
    verification_link
):

    subject = "Verify Your MediLink AI Email"

    html = f"""
    <html>
    <body style="font-family:Arial,sans-serif;">

        <h2 style="color:#1565C0;">
            Welcome to MediLink AI
        </h2>

        <p>
        Thank you for creating an account.
        </p>

        <p>
        Please verify your email address by clicking
        the button below.
        </p>

        <p>

        <a href="{verification_link}"
        style="
            background:#2E7D32;
            color:white;
            padding:12px 20px;
            text-decoration:none;
            border-radius:6px;
            display:inline-block;
        ">

        Verify Email

        </a>

        </p>

        <hr>

        <p style="color:gray;font-size:12px;">
        © 2026 MediLink AI
        </p>

    </body>
    </html>
    """

    return send_email(
        recipient_email,
        subject,
        html
    )

    # ==========================================
# PASSWORD RESET OTP EMAIL
# ==========================================

def send_password_reset_otp_email(
    recipient_email,
    otp
):

    subject = "Your MediLink AI Password Reset Code"

    html = f"""
    <html>
    <body style="font-family:Arial,sans-serif;">

        <h2 style="color:#1565C0;">
            MediLink AI
        </h2>

        <p>Hello,</p>

        <p>
        We received a request to reset your password.
        </p>

        <p>
        Use the verification code below:
        </p>

        <h1 style="
            color:#1565C0;
            letter-spacing:8px;
            font-size:40px;
        ">
            {otp}
        </h1>

        <p>
        This code expires in <b>10 minutes</b>.
        </p>

        <p>
        If you didn't request a password reset,
        simply ignore this email.
        </p>

        <hr>

        <p style="color:gray;font-size:12px;">
        © 2026 MediLink AI
        </p>

    </body>
    </html>
    """

    plain = f"""
Your MediLink AI password reset code is:

{otp}

This code expires in 10 minutes.
"""

    return send_email(
        recipient_email,
        subject,
        html,
        plain
    )