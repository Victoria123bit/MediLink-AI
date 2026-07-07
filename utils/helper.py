import streamlit as st
from datetime import datetime
import random


# ==========================================
# FOOTER
# ==========================================

def footer():

    st.markdown("---")

    st.markdown(
        """
<div style='text-align:center;padding:10px;'>

<h4 style='color:#1565C0;margin-bottom:5px;'>
🏥 MediLink AI
</h4>

<p style='color:gray;'>

AI-Powered Healthcare Assistant for Nigeria 

</p>

<p style='font-size:12px;color:#999;'>

© 2026 MediLink AI. All Rights Reserved.

</p>

</div>
""",
        unsafe_allow_html=True
    )


# ==========================================
# HERO BANNER
# ==========================================

def hero_banner(user_name):

    hour = datetime.now().hour

    if hour < 12:
        greeting = "☀️ Good Morning"
    elif hour < 17:
        greeting = "🌤️ Good Afternoon"
    else:
        greeting = "🌙 Good Evening"

    st.markdown(
        f"""
<div class="hero">

<h1>
🏥 MediLink AI
</h1>

<h3>
Smart Healthcare Guidance for Every Nigerian 🇳🇬
</h3>

<p style="font-size:18px;">

{greeting},
<b>{user_name}</b> 👋

<br><br>

Your trusted AI-powered healthcare companion.

Receive health education, medication reminders,
and AI-powered guidance anytime.

</p>

</div>
""",
        unsafe_allow_html=True
    )


# ==========================================
# HEALTH TIP
# ==========================================

def health_tip():

    tips = [

        "💧 Drink at least 8 glasses of clean water today.",

        "🥗 Eat more fruits and vegetables for better immunity.",

        "🚶 Exercise for at least 30 minutes every day.",

        "😴 Aim for 7–9 hours of quality sleep tonight.",

        "🩺 Visit a healthcare professional for routine checkups.",

        "🦟 Sleep under an insecticide-treated mosquito net.",

        "🧼 Wash your hands regularly with soap and water.",

        "🥛 Stay hydrated, especially during hot weather.",

        "🍎 Reduce sugary drinks and processed foods.",

        "❤️ Your health is your greatest investment."

    ]

    st.success(random.choice(tips))


# ==========================================
# SECTION TITLE
# ==========================================

def section_title(title, icon="✨"):

    st.markdown(
        f"""
<h2 style="margin-top:10px;">

{icon} {title}

</h2>
""",
        unsafe_allow_html=True
    )


# ==========================================
# FEATURE CARD
# ==========================================

def feature_card(title, description, emoji):

    st.markdown(
        f"""
<div class="health-card">

<h3>{emoji} {title}</h3>

<p>

{description}

</p>

</div>
""",
        unsafe_allow_html=True
    )


# ==========================================
# WELCOME MESSAGE
# ==========================================

def welcome_banner():

    hero_banner(st.session_state.full_name)