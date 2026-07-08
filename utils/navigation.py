import streamlit as st

from auth.auth import logout


# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

def show_sidebar():

    # ==========================================
    # LOGO
    # ==========================================

    st.sidebar.image(
        "assets/logo.png",
        width=170
    )

    st.sidebar.markdown("---")


    # ==========================================
    # USER INFORMATION
    # ==========================================

    full_name = st.session_state.get(
        "full_name",
        "User"
    )

    st.sidebar.success(
        f"👋 Welcome\n\n**{full_name}**"
    )

    st.sidebar.info(
        "🟢 Account Active"
    )


    st.sidebar.markdown("---")


    # ==========================================
    # NAVIGATION MENU
    # ==========================================

    st.sidebar.markdown(
        "### 📌 MediLink AI"
    )


    selected_page = st.sidebar.radio(
        "Navigate",
        [
            "🏠 Home",
            "🤖 Symptom Checker",
            "📚 Health Education",
            "💊 Medication Reminder",
            "📊 Dashboard",
            "🚑 Emergency Hospitals",
            "👤 My Profile",
            "ℹ️ About"
        ]
    )


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
        st.rerun()


    return selected_page