import streamlit as st
from database.database import login_user


# ==========================================
# LOGIN PAGE
# ==========================================

def login_page():

    st.title("🔐 Login to MediLink AI")

    st.markdown("""
Welcome back! 👋

Sign in to continue accessing your personal healthcare dashboard.
""")

    st.divider()

    # ===============================
    # LOGIN FORM
    # ===============================

    email = st.text_input(
        "📧 Email Address",
        placeholder="Enter your email"
    )

    password = st.text_input(
        "🔒 Password",
        type="password",
        placeholder="Enter your password"
    )

    # ===============================
    # FORGOT PASSWORD
    # ===============================

    if st.button(
        "🔑 Forgot Password?",
        use_container_width=True
    ):
        st.session_state.show_forgot_password = True
        st.rerun()

    st.divider()

    # ===============================
    # LOGIN BUTTON
    # ===============================

    if st.button(
        "🔐 Login",
        use_container_width=True,
        type="primary"
    ):

        email = email.strip().lower()

        if not email or not password:
            st.error("⚠️ Please enter both your email address and password.")
            return

        with st.spinner("Signing you in..."):

            user = login_user(email, password)

        if user:

            st.session_state.logged_in = True
            st.session_state.user_id = user["id"]
            st.session_state.full_name = user["full_name"]
            st.session_state.email = user["email"]

            st.success(
                f"✅ Welcome back, {user['full_name']}!"
)

            st.balloons()

            st.rerun()

        else:

            st.error("❌ Invalid email or password.")

    st.markdown("---")

    st.caption(
        "🔒 Your account is securely protected and your personal information remains private."
    )