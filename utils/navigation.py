import streamlit as st

from auth.auth import logout


# ==========================================
# SIDEBAR NAVIGATION
# ==========================================

def show_sidebar():

    # Always show the sidebar expanded on desktop
    st.set_page_config(
        initial_sidebar_state="expanded"
    )

    with st.sidebar:

        st.image(
            "assets/logo.png",
            width=170
        )

        st.markdown("---")

        full_name = st.session_state.get(
            "full_name",
            "User"
        )

        st.success(
            f"👋 Welcome\n\n**{full_name}**"
        )

        st.info("🟢 Account Active")

        st.markdown("---")

        st.markdown("### 📌 MediLink AI")

        pages = {
            "🏠 Home": "pages/1_Home.py",
            "🤖 Symptom Checker": "pages/2_Symptom_Checker.py",
            "📚 Health Education": "pages/3_Health_Education.py",
            "💊 Medication Reminder": "pages/4_Medication_Reminder.py",
            "📊 Dashboard": "pages/5_Dashboard.py",
            "🚑 Emergency Hospitals": "pages/7_Emergency_Hospitals.py",
            "👤 My Profile": "pages/8_My_Profile.py",
            "ℹ️ About": "pages/6_About.py"
        }

        selected = st.radio(
            "Navigate",
            list(pages.keys()),
            label_visibility="collapsed"
        )

        if st.button(
            "🚪 Logout",
            use_container_width=True,
            type="primary"
        ):
            logout()

    # Switch pages
    current = st.session_state.get("current_page")

    if current != selected:

        st.session_state.current_page = selected

        st.switch_page(
            pages[selected]
        )

    return selected