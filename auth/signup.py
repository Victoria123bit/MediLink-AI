import streamlit as st
from database.database import register_user
import re


# ==========================================
# SIGNUP PAGE
# ==========================================

def signup_page():

    st.title("📝 Create Your MediLink AI Account")

    st.markdown("""
Welcome to **MediLink AI** 👋

Create your free account to access AI-powered healthcare guidance, medication reminders, and personalized health tools.
""")

    st.divider()

    # ==========================================
    # USER DETAILS
    # ==========================================

    col1, col2 = st.columns(2)

    with col1:

        full_name = st.text_input(
            "👤 Full Name",
            placeholder="Enter your full name"
        )

        email = st.text_input(
            "📧 Email Address",
            placeholder="example@email.com"
        )

        phone = st.text_input(
            "📱 Phone Number",
            placeholder="08012345678"
        )

    with col2:

        age = st.number_input(
            "🎂 Age",
            min_value=1,
            max_value=120,
            step=1
        )

        gender = st.selectbox(
            "🚻 Gender",
            [
                "Male",
                "Female",
                "Prefer not to say"
            ]
        )

    password = st.text_input(
        "🔒 Password",
        type="password",
        placeholder="Create a strong password"
    )

    confirm_password = st.text_input(
        "🔒 Confirm Password",
        type="password",
        placeholder="Re-enter your password"
    )

    st.divider()

    # ==========================================
    # CREATE ACCOUNT BUTTON
    # ==========================================

    if st.button(
        "📝 Create Account",
        use_container_width=True,
        type="primary"
    ):

        full_name = full_name.strip()
        email = email.strip().lower()
        phone = phone.strip()

        # ==========================================
        # VALIDATION
        # ==========================================

        if not all([full_name, email, phone, password, confirm_password]):
            st.error("⚠️ Please complete all required fields.")
            return

        # Email validation
        email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

        if not re.match(email_pattern, email):
            st.error("❌ Please enter a valid email address.")
            return

        # Nigerian phone number validation
        if not phone.isdigit() or len(phone) != 11:
            st.error("❌ Please enter a valid 11-digit Nigerian phone number.")
            return

        # Password match
        if password != confirm_password:
            st.error("❌ Passwords do not match.")
            return

        # Password strength
        if len(password) < 8:
            st.error("❌ Password must contain at least 8 characters.")
            return

        # ==========================================
        # REGISTER USER
        # ==========================================

        with st.spinner("Creating your account..."):

            success = register_user(
                full_name,
                email,
                phone,
                age,
                gender,
                password
            )

        if success:

            st.success("🎉 Your account has been created successfully!")

            st.balloons()

            st.info("✅ You can now log in using your email and password.")

        else:

            st.error("❌ An account with this email already exists.")

    st.markdown("---")

    st.caption(
        "🔒 Your personal information is securely stored and protected."
    )