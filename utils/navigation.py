import streamlit as st

from auth.auth import logout


# ==========================================
# SIDEBAR
# ==========================================

def show_sidebar():

    # ==========================================
    # LOGO
    # ==========================================

    st.sidebar.image("assets/logo.png", width=170)

    st.sidebar.markdown("---")

    # ==========================================
    # USER INFORMATION
    # ==========================================

    full_name = st.session_state.get("full_name", "User")

    st.sidebar.success(
        f"👋 Welcome\n\n**{full_name}**"
    )

    st.sidebar.info("🟢 Account Active")

    st.sidebar.markdown("---")

    # ==========================================
    # APPLICATION
    # ==========================================

    st.sidebar.markdown("### 📌 MediLink AI")

    st.sidebar.write("🏠 Home")
    st.sidebar.write("🤖 Symptom Checker")
    st.sidebar.write("📚 Health Education")
    st.sidebar.write("💊 Medication Reminder")
    st.sidebar.write("📊 Dashboard")
    st.sidebar.write("🚑 Emergency Hospitals")
    st.sidebar.write("👤 My Profile")
    st.sidebar.write("ℹ️ About")

    st.sidebar.markdown("---")

    # ==========================================
    # LOGOUT
    # ==========================================

    if st.sidebar.button(
        "🚪 Logout",
        use_container_width=True,
        type="primary"
    ):
        logout()