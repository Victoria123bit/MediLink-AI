import streamlit as st
from datetime import datetime

from auth.auth import check_login
from utils.navigation import show_navigation

from database.database import (
    get_user_profile,
    get_total_reminders,
    get_total_ai_checks
)

from utils.helper import (
    footer,
    section_title
)

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="My Profile | MediLink AI",
    page_icon="👤",
    layout="wide"
)

# ==========================================
# HIDE STREAMLIT SIDEBAR
# ==========================================

st.markdown("""
<style>

/* Hide Streamlit Sidebar */
[data-testid="stSidebar"]{
    display:none;
}

/* Hide Sidebar Toggle Button */
[data-testid="stSidebarCollapsedControl"]{
    display:none;
}

/* Remove left spacing */
section.main{
    margin-left:0rem;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# PROTECT PAGE
# ==========================================

if not check_login():
    st.switch_page("MediLink_AI.py")

# ==========================================
# SIDEBAR
# ==========================================

show_navigation()

# ==========================================
# LOAD USER PROFILE
# ==========================================

user = get_user_profile(
    st.session_state.user_id
)

# ==========================================
# HERO SECTION
# ==========================================

st.markdown("""
<div class="hero">

<h1>👤 My Profile</h1>

<h3>Your Personal Healthcare Account</h3>

<p style="font-size:18px;">

Manage your MediLink AI profile and monitor your healthcare activities.

</p>

</div>
""", unsafe_allow_html=True)

# ==========================================
# PROFILE HEADER
# ==========================================

col1, col2 = st.columns([1, 3])

with col1:

    st.markdown(
        "<h1 style='font-size:80px;text-align:center;'>👤</h1>",
        unsafe_allow_html=True
    )

with col2:

    st.markdown(f"""
### {user["full_name"]}

🟢 **Verified Member**

📧 {user["email"]}
""")

st.divider()

# ==========================================
# PERSONAL INFORMATION
# ==========================================

section_title("Personal Information", "📄")

col1, col2 = st.columns(2)

with col1:

   st.info(f"""
### 👤 Full Name

{user["full_name"]}
""")

   st.info(f"""
### 📱 Phone Number

{user["phone"]}
""")

   st.info(f"""
### 🎂 Age

{user["age"]} Years
""")

with col2:

    st.info(f"""
### 🚻 Gender

{user["gender"]}
""")

    st.info(f"""
### 📅 Member Since

{user["created_at"][:10]}
""")

    st.info("""
### 🟢 Status

Active
""")

st.divider()

# ==========================================
# ACCOUNT ACTIVITY
# ==========================================

section_title("Account Activity", "📊")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "💊 Reminders",
        get_total_reminders(
            st.session_state.user_id
        )
    )

with col2:

    st.metric(
        "🤖 AI Checks",
        get_total_ai_checks(
            st.session_state.user_id
        )
    )

with col3:

    days = (
    datetime.now() -
    datetime.strptime(
        user["created_at"][:10],
        "%Y-%m-%d"
    )
).days
    st.metric(
        "📅 Days With Us",
        days
    )

st.divider()

# ==========================================
# ACCOUNT SECURITY
# ==========================================

section_title("Account Security", "🔐")

st.success("""

✅ Password securely encrypted

✅ Secure login authentication

✅ Personal information stored securely

✅ Protected database

""")

st.divider()

# ==========================================
# PRIVACY NOTICE
# ==========================================

section_title("Privacy Notice", "🛡️")

st.info("""

Your information is used only to personalize your experience within MediLink AI.

We do not sell or share your personal information.

Always use a strong password to keep your account secure.

""")

st.divider()

# ==========================================
# MEMBER BENEFITS
# ==========================================

section_title("Your Benefits", "🎁")

left, right = st.columns(2)

with left:

    st.success("""

✔ AI Symptom Checker

✔ Health Education

✔ Medication Reminders

✔ Emergency Support

""")

with right:

    st.info("""

✔ Personal Dashboard

✔ Secure Account

✔ AI Health Reports

✔ Future Updates

""")

st.divider()

# ==========================================
# FOOTER
# ==========================================

footer()