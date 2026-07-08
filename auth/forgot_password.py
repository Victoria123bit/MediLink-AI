import streamlit as st

from database.database import (
    email_exists,
    create_password_reset_otp,
    verify_password_reset_otp,
    delete_password_reset_otp,
    update_password
)

from utils.email_service import (
    send_password_reset_otp_email
)


# ==========================================
# FORGOT PASSWORD
# ==========================================

def forgot_password_page():

    st.title("🔑 Forgot Password")

    # Initialize session state
    if "otp_sent" not in st.session_state:
        st.session_state.otp_sent = False

    if "reset_email" not in st.session_state:
        st.session_state.reset_email = ""

    # ==========================================
    # STEP 1 - ENTER EMAIL
    # ==========================================

    if not st.session_state.otp_sent:

        email = st.text_input(
            "📧 Email Address",
            placeholder="Enter your registered email"
        )

        if st.button(
            "📩 Send Verification Code",
            use_container_width=True
        ):

            email = email.strip().lower()

            if email == "":
                st.error("Please enter your email.")
                return

            if not email_exists(email):
                st.error("No account found with this email.")
                return

            otp = create_password_reset_otp(email)

            success = send_password_reset_otp_email(
                email,
                otp
            )

            if success:

                st.session_state.otp_sent = True
                st.session_state.reset_email = email

                st.success(
                    "✅ Verification code sent to your email."
                )

                st.rerun()

            else:

                st.error("Unable to send email.")

    # ==========================================
    # STEP 2 - VERIFY OTP
    # ==========================================

    else:

        st.success(
            f"Verification code sent to:\n\n{st.session_state.reset_email}"
        )

        otp = st.text_input(
            "Enter 6-digit verification code"
        )

        new_password = st.text_input(
            "New Password",
            type="password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password"
        )

        if st.button(
            "✅ Reset Password",
            use_container_width=True
        ):

            if not verify_password_reset_otp(
                st.session_state.reset_email,
                otp
            ):

                st.error("Invalid or expired verification code.")
                return

            if len(new_password) < 8:

                st.error(
                    "Password must be at least 8 characters."
                )
                return

            if new_password != confirm_password:

                st.error("Passwords do not match.")
                return

            update_password(
                st.session_state.reset_email,
                new_password
            )

            delete_password_reset_otp(
                st.session_state.reset_email
            )

            st.success("✅ Password updated successfully!")

            st.session_state.otp_sent = False
            st.session_state.reset_email = ""
            st.session_state.show_forgot_password = False

            st.info("You can now log in.")

        if st.button("⬅ Back"):

            st.session_state.otp_sent = False
            st.session_state.reset_email = ""

            st.rerun()