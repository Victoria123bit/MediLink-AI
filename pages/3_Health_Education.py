import streamlit as st

from auth.auth import check_login
from utils.navigation import show_navigation

from ai.gemini import model

from utils.helper import (
    footer,
    section_title
)

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Health Education | MediLink AI",
    page_icon="📚",
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
# HERO SECTION
# ==========================================

st.markdown("""
<div class="hero">

<h1>📚 Health Education</h1>

<h3>Learn • Prevent • Stay Healthy</h3>

<p style="font-size:18px;">

Reliable AI-powered health education designed for Nigerians.

</p>

</div>
""", unsafe_allow_html=True)

# ==========================================
# INTRODUCTION
# ==========================================

st.info(f"""
👋 **Welcome {st.session_state.full_name}!**

Choose any health topic below and MediLink AI will explain it in simple, easy-to-understand language.

⚠️ This information is for educational purposes only and is **not** medical advice.
""")

# ==========================================
# HEALTH TOPICS
# ==========================================

section_title("Choose a Health Topic", "📖")

topics = [

    "Malaria",
    "Typhoid Fever",
    "Diabetes",
    "Hypertension",
    "Asthma",
    "Tuberculosis",
    "Cholera",
    "Mental Health",
    "Pregnancy Care",
    "Child Health",
    "Nutrition",
    "Exercise",
    "First Aid",
    "Healthy Living",
    "Food Safety",
    "Water Hygiene"

]

selected_topic = st.selectbox(
    "",
    topics
)

st.write("")

# ==========================================
# GENERATE LESSON
# ==========================================

if st.button(
    "📘 Learn About This Topic",
    use_container_width=True
):

    with st.spinner("🤖 MediLink AI is preparing your lesson..."):

        prompt = f"""
You are MediLink AI, an AI healthcare education assistant designed specifically for people living in Nigeria.

Explain the following health topic:

{selected_topic}

Use these headings exactly:

# 📖 Overview

# ⚠️ Causes or Risk Factors

# 🩺 Common Symptoms

# 🛡️ Prevention

# 👨‍⚕️ When to Visit a Healthcare Professional

# 🇳🇬 Nigerian Health Tips

Rules:

- Use simple English.
- Never diagnose diseases.
- Never prescribe medications.
- Keep the information educational.
- Use bullet points where appropriate.
"""

        try:

            response = model.generate_content(prompt)

            st.success("✅ Lesson Ready")

            st.markdown(response.text)

        except Exception as e:

            error = str(e)

            if "429" in error:

                st.warning("""
⚠️ MediLink AI has temporarily reached its AI request limit.

Please wait about one minute and try again.

This only affects the AI feature temporarily.
""")

            else:

                st.error("❌ Unable to contact Gemini AI.")

                with st.expander("Technical Details"):
                    st.code(error)

st.divider()

# ==========================================
# QUICK HEALTH FACTS
# ==========================================

section_title("Quick Health Facts", "💡")

col1, col2 = st.columns(2)

with col1:

    st.success("""
### 🦟 Malaria Prevention

• Sleep under insecticide-treated mosquito nets.

• Remove stagnant water around your home.

• Use mosquito repellents.

• Visit a hospital if fever persists.
""")

    st.success("""
### 🥗 Healthy Eating

• Eat fruits every day.

• Eat vegetables regularly.

• Drink enough clean water.

• Reduce sugary drinks and processed foods.
""")

with col2:

    st.info("""
### ❤️ Heart Health

• Exercise regularly.

• Reduce salt intake.

• Avoid smoking.

• Check your blood pressure regularly.
""")

    st.info("""
### 🧼 Personal Hygiene

• Wash your hands frequently.

• Drink clean water.

• Wash fruits before eating.

• Practice safe food handling.
""")

st.divider()

# ==========================================
# HEALTHY NIGERIA
# ==========================================

section_title("Healthy Nigeria Tips", "🌍")

st.warning("""
✔ Visit your nearest Primary Health Centre (PHC) for regular check-ups.

✔ Complete childhood immunizations.

✔ Sleep under treated mosquito nets.

✔ Drink safe, clean water.

✔ Wash your hands regularly with soap.

✔ Avoid self-medication.

✔ Attend antenatal care during pregnancy.

✔ Exercise for at least 30 minutes daily.

✔ Eat balanced meals.

✔ Go for routine medical check-ups.
""")

st.divider()

# ==========================================
# DISCLAIMER
# ==========================================

st.warning("""
### ⚠️ Medical Disclaimer

The information provided by MediLink AI is for educational purposes only.

It does **NOT** diagnose diseases, prescribe medications, or replace qualified healthcare professionals.

Always consult a licensed healthcare professional for proper diagnosis and treatment.
""")

# ==========================================
# FOOTER
# ==========================================

footer()