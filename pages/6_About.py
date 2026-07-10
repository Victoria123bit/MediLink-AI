import streamlit as st

from auth.auth import check_login
from utils.navigation import show_navigation

from utils.helper import (
    footer,
    section_title
)

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="About | MediLink AI",
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
# HERO
# ==========================================

st.markdown("""
<div class="hero">

<h1>🏥 About MediLink AI</h1>

<h3>Smart Healthcare Guidance for Every Nigerian 🇳🇬</h3>

<p style="font-size:18px;">

Making healthcare education more accessible through Artificial Intelligence.

</p>

</div>
""", unsafe_allow_html=True)

# ==========================================
# ABOUT
# ==========================================

section_title("Who We Are", "🌍")

st.markdown("""
MediLink AI is an AI-powered healthcare education platform designed to help people in Nigeria access reliable health information anytime and anywhere.

Using **AI Service**, MediLink AI provides educational guidance, symptom awareness, medication reminders, health education, and emergency healthcare resources.

Our goal is to improve health awareness while encouraging users to seek professional medical care whenever necessary.
""")

st.divider()

# ==========================================
# MISSION & VISION
# ==========================================

col1, col2 = st.columns(2)

with col1:

    section_title("Our Mission", "🎯")

    st.success("""

To improve healthcare awareness across Nigeria by providing easy-to-understand, AI-powered educational information that empowers people to make informed health decisions.

""")

with col2:

    section_title("Our Vision", "👁️")

    st.info("""

To become one of Africa's leading AI healthcare education platforms, making reliable health knowledge accessible to everyone.

""")

st.divider()

# ==========================================
# FEATURES
# ==========================================

section_title("Key Features", "⭐")

c1, c2 = st.columns(2)

with c1:

    st.success("""

🤖 AI Symptom Checker

📚 Health Education

💊 Medication Reminders

📊 Personal Dashboard

""")

with c2:

    st.info("""

🚑 Emergency Hospitals

👤 Secure User Profiles

🔐 Password Encryption

📄 AI Health Reports

""")

st.divider()

# ==========================================
# TECHNOLOGY STACK
# ==========================================

section_title("Technology Stack", "💻")

st.markdown("""

MediLink AI was developed using modern technologies:

- 🐍 Python
- 🎨 Streamlit
- 🤖 Groq AI
- 🗄 SQLite Database
- 📊 Plotly
- 🔒 bcrypt Password Encryption
- ☁️ Streamlit Community Cloud

""")

st.divider()

# ==========================================
# WHY NIGERIA
# ==========================================

section_title("Why MediLink AI for Nigeria?", "🇳🇬")

st.warning("""

Nigeria faces several healthcare challenges including:

✔ Limited access to healthcare information

✔ Shortage of healthcare professionals

✔ Late hospital visits

✔ Self-medication

✔ Poor health awareness

MediLink AI aims to bridge this gap by providing instant educational healthcare guidance while encouraging professional medical consultation.

""")

st.divider()

# ==========================================
# FUTURE FEATURES
# ==========================================

section_title("Future Improvements", "🚀")

st.info("""

Coming soon:

✅ Hospital Appointment Booking

✅ Drug Interaction Checker

✅ Voice-Based AI Assistant

✅ AI Medical Report Analysis

✅ Multi-language Support

✅ Offline Health Education

✅ Vaccination Tracker

✅ Health Risk Prediction

""")

st.divider()

# ==========================================
# DEVELOPER
# ==========================================

section_title("Developer", "👩‍💻")

st.success("""

**Victoria Ayomide Odumosu**

AI & Data Science Enthusiast

3MTT Fellow

Passionate about building AI solutions that solve real-world healthcare problems in Nigeria.

""")

st.divider()

# ==========================================
# ACKNOWLEDGEMENTS
# ==========================================

section_title("Acknowledgements", "❤️")

st.markdown("""

Special thanks to:

- Groq AI

- Streamlit

- Python Community

- Plotly

- SQLite

- 3MTT Nigeria

- Healthcare professionals whose knowledge inspires responsible AI health education.

""")

st.divider()

# ==========================================
# DISCLAIMER
# ==========================================

st.warning("""

### ⚠️ Medical Disclaimer

MediLink AI provides educational health information only.

It does **NOT** diagnose diseases, prescribe medications, or replace qualified healthcare professionals.

Always seek advice from a licensed healthcare provider for diagnosis and treatment.

""")

# ==========================================
# FOOTER
# ==========================================

footer()