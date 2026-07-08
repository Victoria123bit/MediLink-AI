import streamlit as st
from datetime import datetime

from auth.auth import check_login
from utils.navigation import show_navigation

from database.database import (
    get_total_reminders,
    get_total_users,
    get_total_ai_checks
)

from utils.helper import (
    hero_banner,
    footer,
    health_tip,
    feature_card,
    section_title
)

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Home | MediLink AI",
    page_icon="🏥",
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
# HERO BANNER
# ==========================================

hero_banner(st.session_state.full_name)

# ==========================================
# QUICK STATS
# ==========================================

section_title("Your Healthcare Overview", "📊")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💊 Reminders",
        get_total_reminders(st.session_state.user_id)
    )

with col2:
    st.metric(
        "🤖 AI Checks",
        get_total_ai_checks(st.session_state.user_id)
    )

with col3:
    st.metric(
        "📚 Health Topics",
        "12+"
    )

with col4:
    st.metric(
        "👥 Registered Users",
        get_total_users()
    )

st.write("")

# ==========================================
# FEATURES
# ==========================================

section_title("Explore MediLink AI", "🚀")

c1, c2, c3 = st.columns(3)

with c1:
    feature_card(
        "AI Symptom Checker",
        "Describe your symptoms and receive educational AI-powered health guidance in seconds.",
        "🤖"
    )

with c2:
    feature_card(
        "Health Education",
        "Learn about malaria, diabetes, hypertension, maternal care, nutrition and many other health conditions.",
        "📚"
    )

with c3:
    feature_card(
        "Medication Reminder",
        "Save your medications and never miss another dose.",
        "💊"
    )

c4, c5, c6 = st.columns(3)

with c4:
    feature_card(
        "Dashboard",
        "Monitor your reminders and AI healthcare activities from one place.",
        "📊"
    )

with c5:
    feature_card(
        "Emergency Hospitals",
        "Quickly access emergency contacts and nearby hospitals.",
        "🚑"
    )

with c6:
    feature_card(
        "My Profile",
        "Manage your healthcare account securely.",
        "👤"
    )

st.write("")

# ==========================================
# WHY CHOOSE MEDILINK AI
# ==========================================

section_title("Why Choose MediLink AI?", "❤️")

left, right = st.columns(2)

with left:

    st.success("""
✅ AI-Powered Healthcare Education

✅ Designed for Nigerians

✅ Secure User Accounts

✅ Medication Reminders

✅ Emergency Health Information

✅ Fast AI Responses
""")

with right:

    st.info("""
🌍 Powered by Google Gemini AI

🔒 Secure Password Encryption

🏥 Nigerian Healthcare Focus

📱 Mobile Friendly

⚡ Fast Performance

💚 Free to Use
""")

st.write("")

# ==========================================
# HEALTH TIP
# ==========================================

section_title("Health Tip of the Day", "💡")

health_tip()

# ==========================================
# DAILY MOTIVATION
# ==========================================

quotes = [

    "💙 Good health is the foundation of a happy life.",

    "🥗 Healthy eating is a form of self-respect.",

    "🚶 Small healthy habits create big results.",

    "💧 Water is one of the body's best medicines.",

    "😴 Quality sleep is essential for good health.",

    "❤️ Prevention is always better than cure.",

    "🌿 A healthy lifestyle starts one healthy choice at a time."

]

today = datetime.now().day

st.info(
    f"### 🌟 Daily Inspiration\n\n{quotes[today % len(quotes)]}"
)

# ==========================================
# GETTING STARTED
# ==========================================

section_title("Getting Started", "🎯")

st.markdown("""

### Follow these simple steps

**1️⃣ AI Symptom Checker**

Describe your symptoms and receive AI-powered educational health guidance.

---

**2️⃣ Health Education**

Learn about common diseases affecting Nigerians.

---

**3️⃣ Medication Reminder**

Save your medication schedule and receive reminders.

---

**4️⃣ Dashboard**

Track your healthcare activities.

---

**5️⃣ Emergency Hospitals**

Quickly access emergency contacts and nearby hospitals when needed.

""")

# ==========================================
# DISCLAIMER
# ==========================================

st.warning("""
### ⚠️ Medical Disclaimer

MediLink AI provides educational healthcare information only.

It does **NOT** diagnose diseases, prescribe medications, or replace qualified healthcare professionals.

Always consult a licensed healthcare provider for proper diagnosis and treatment.
""")

# ==========================================
# FOOTER
# ==========================================

footer()