import streamlit as st

from database.database import create_database
from auth.login import login_page
from auth.signup import signup_page
from auth.forgot_password import forgot_password_page
from auth.auth import check_login
from utils.navigation import show_navigation

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="MediLink AI",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================
# HIDE STREAMLIT SIDEBAR
# ==========================================

st.markdown("""
<style>

/* Hide the Streamlit sidebar */
[data-testid="stSidebar"]{
    display:none;
}

/* Hide the expand/collapse button */
[data-testid="stSidebarCollapsedControl"]{
    display:none;
}

/* Remove left margin */
section.main{
    margin-left:0rem;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# LOAD CSS
# ==========================================

def load_css():
    try:
        with open("assets/style.css", encoding="utf-8") as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )
    except FileNotFoundError:
        st.warning("style.css not found.")


load_css()

# ==========================================
# CREATE DATABASE
# ==========================================

create_database()

params = st.query_params

if params.get("page") == "9_Reset_Password":
    st.switch_page("pages/9_Reset_Password.py")

# ==========================================
# SESSION VARIABLES
# ==========================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user_id" not in st.session_state:
    st.session_state.user_id = None

if "full_name" not in st.session_state:
    st.session_state.full_name = ""

if "email" not in st.session_state:
    st.session_state.email = ""

if "show_forgot_password" not in st.session_state:
    st.session_state.show_forgot_password = False

# ==========================================
# LOGIN / SIGNUP SCREEN
# ==========================================

if not check_login():

    left, right = st.columns([1.2, 1])

    with left:

        st.markdown("""
<div class="hero">

<h1>🏥 MediLink AI</h1>

<h3>Smart Healthcare Guidance for Every Nigerian</h3>

<p style="font-size:18px;">

Get instant AI-powered healthcare education,
symptom guidance, medication reminders
and trusted health information.

</p>

</div>
""", unsafe_allow_html=True)

        st.markdown("### 🌟 Why Choose MediLink AI?")

        st.success("🤖 AI-Powered Symptom Checker")
        st.success("📚 Health Education")
        st.success("💊 Medication Reminders")
        st.success("🚑 Emergency Hospital Finder")
        st.success("🔒 Secure Personal Health Account")

    with right:

        st.markdown("## Welcome 👋")

        option = st.radio(
            "",
            [
                "🔐 Login",
                "📝 Create Account"
            ]
        )

        if option == "🔐 Login":

            if st.session_state.show_forgot_password:
                forgot_password_page()
            else:
                login_page()

        else:

            signup_page()

    st.stop()

# ==========================================
# LOGGED-IN HOME SCREEN
# ==========================================

show_navigation()

st.info("""
### 🚀 Getting Started

Use the **navigation menu above** to access all MediLink AI features.

You can:

- 🤖 Analyze symptoms
- 📚 Learn about diseases
- 💊 Save medication reminders
- 📊 View your dashboard
- 🚑 Find emergency hospitals
- 👤 Manage your profile
""")

st.warning("""
### ⚠️ Medical Disclaimer

MediLink AI provides educational health information only.

It does **NOT** diagnose diseases or replace qualified healthcare professionals.

Always consult a licensed healthcare provider for diagnosis and treatment.
""")

st.markdown("---")

st.markdown(
    """
<div style="text-align:center">

<h4 style="color:#1565C0;">
🏥 MediLink AI
</h4>

<p style="color:gray;">

© 2026 MediLink AI

</p>

</div>
""",
    unsafe_allow_html=True
)