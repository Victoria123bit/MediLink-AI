import streamlit as st

from auth.auth import check_login
from utils.navigation import show_sidebar

from utils.helper import (
    footer,
    section_title
)

# ==========================================
# PROTECT PAGE
# ==========================================

if not check_login():
    st.switch_page("MediLink_AI.py")

# ==========================================
# SIDEBAR
# ==========================================

show_sidebar()

# ==========================================
# HERO
# ==========================================

st.markdown("""
<div class="hero">

<h1>🚑 Emergency Hospitals</h1>

<h3>Emergency Support When Every Second Counts</h3>

<p style="font-size:18px;">

Quickly access emergency contacts and locate nearby hospitals.

</p>

</div>
""", unsafe_allow_html=True)

# ==========================================
# INTRODUCTION
# ==========================================

st.info(f"""
👋 **Welcome {st.session_state.full_name}!**

If you or someone around you has a medical emergency, seek professional medical care immediately.
""")

# ==========================================
# EMERGENCY NUMBERS
# ==========================================

section_title("Emergency Numbers", "📞")

col1, col2, col3 = st.columns(3)

with col1:

    st.error("""
### 🚑 Ambulance

# **112**
""")

with col2:

    st.warning("""
### 🚓 Police

# **112**
""")

with col3:

    st.info("""
### 🚒 Fire Service

# **112**
""")

st.divider()

# ==========================================
# FIND HOSPITAL
# ==========================================

section_title("Locate a Nearby Hospital", "📍")

st.write(
    "Use Google Maps to locate hospitals close to your current location."
)

st.link_button(
    "🏥 Find Hospitals Near Me",
    "https://www.google.com/maps/search/hospitals+near+me",
    use_container_width=True
)

st.divider()

# ==========================================
# WHEN TO SEEK EMERGENCY CARE
# ==========================================

section_title("Seek Emergency Care Immediately If...", "🚨")

st.error("""

• Difficulty breathing

• Severe chest pain

• Heavy bleeding

• Loss of consciousness

• Seizures

• Stroke symptoms

• Serious burns

• Severe allergic reactions

• Poisoning

• Serious road traffic accidents

""")

st.divider()

# ==========================================
# FIRST AID
# ==========================================

section_title("Basic First Aid Tips", "🩹")

col1, col2 = st.columns(2)

with col1:

    st.success("""

### ❤️ Stay Calm

✔ Call for help immediately.

✔ Keep the patient comfortable.

✔ Do not panic.

✔ Reassure the patient.

""")

    st.success("""

### 🩸 Bleeding

✔ Apply firm pressure.

✔ Elevate the injured part if possible.

✔ Use a clean cloth or bandage.

""")

with col2:

    st.info("""

### 🔥 Burns

✔ Cool with running water.

✔ Do not apply oil or toothpaste.

✔ Cover with a clean cloth.

""")

    st.info("""

### 😮 Choking

✔ Encourage coughing.

✔ Seek emergency help immediately.

✔ Perform first aid only if trained.

""")

st.divider()

# ==========================================
# NIGERIA EMERGENCY ADVICE
# ==========================================

section_title("Nigeria Emergency Advice", "🌍")

st.warning("""

✔ Know the nearest government hospital.

✔ Save emergency numbers on your phone.

✔ Keep a basic first aid kit at home.

✔ Visit the nearest Primary Health Centre (PHC) when appropriate.

✔ In life-threatening emergencies, call emergency services immediately.

""")

st.divider()

# ==========================================
# DISCLAIMER
# ==========================================

st.warning("""

### ⚠️ Medical Disclaimer

The information provided here is for educational purposes only.

It should not replace emergency medical services.

If you believe someone is experiencing a medical emergency, contact emergency services or go to the nearest hospital immediately.

""")

# ==========================================
# FOOTER
# ==========================================

footer()