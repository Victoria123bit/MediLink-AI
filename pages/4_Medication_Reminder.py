import streamlit as st
from datetime import datetime

from auth.auth import check_login
from utils.navigation import show_sidebar

from database.database import (
    add_reminder,
    get_reminders
)

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
# HERO SECTION
# ==========================================

st.markdown("""
<div class="hero">

<h1>💊 Medication Reminder</h1>

<h3>Never Miss Your Medication Again</h3>

<p style="font-size:18px;">

Create medication reminders and stay consistent with your treatment.

</p>

</div>
""", unsafe_allow_html=True)

# ==========================================
# INTRODUCTION
# ==========================================

st.info(f"""
👋 **Welcome {st.session_state.full_name}!**

Add your medications below and keep track of your treatment schedule.
""")

# ==========================================
# ADD REMINDER
# ==========================================

section_title("Add New Reminder", "➕")

with st.form("reminder_form"):

    col1, col2 = st.columns(2)

    with col1:

        medication = st.text_input(
            "💊 Medication Name",
            placeholder="e.g. Paracetamol"
        )

        dosage = st.text_input(
            "📝 Dosage",
            placeholder="e.g. 2 Tablets"
        )

    with col2:

        reminder_time = st.time_input(
            "⏰ Reminder Time",
            value=datetime.now().time()
        )

    submitted = st.form_submit_button(
        "💾 Save Reminder",
        use_container_width=True
    )

# ==========================================
# SAVE REMINDER
# ==========================================

if submitted:

    if medication.strip() == "" or dosage.strip() == "":

        st.error("⚠️ Please complete all fields.")

    else:

        add_reminder(
            st.session_state.user_id,
            medication.strip(),
            dosage.strip(),
            str(reminder_time)
        )

        st.success("✅ Medication reminder saved successfully!")

        st.balloons()

        st.rerun()

# ==========================================
# REMINDER SUMMARY
# ==========================================

reminders = get_reminders(st.session_state.user_id)

st.divider()

section_title("Reminder Summary", "📊")

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "💊 Total Medications",
        len(reminders)
    )

with col2:

    st.metric(
        "📅 Today's Date",
        datetime.now().strftime("%d %b %Y")
    )

# ==========================================
# MY REMINDERS
# ==========================================

st.divider()

section_title("My Medication Schedule", "📋")

if reminders:

    for reminder in reminders:

        st.markdown(f"""
<div class="health-card">

<h3>💊 {reminder["medication"]}</h3>

<p>

<b>Dosage:</b> {reminder["dosage"]}

<br><br>

<b>Reminder Time:</b> ⏰ {reminder["reminder_time"]}

</p>

</div>
""", unsafe_allow_html=True)

else:

    st.info("""
You haven't added any medication reminders yet.

Click **Save Reminder** above to create your first reminder.
""")

# ==========================================
# MEDICATION SAFETY TIPS
# ==========================================

st.divider()

section_title("Medication Safety Tips", "💡")

st.success("""

✅ Take medicines exactly as prescribed.

✅ Never skip doses without medical advice.

✅ Do not share medications with others.

✅ Store medicines away from children.

✅ Check expiry dates before use.

✅ Drink enough clean water unless advised otherwise.

""")

# ==========================================
# DISCLAIMER
# ==========================================

st.divider()

st.warning("""

### ⚠️ Medical Disclaimer

Medication reminders are provided only to help you remember your medication schedule.

Always follow the instructions given by your doctor or pharmacist.

Do not change or stop your medication without professional medical advice.

""")

# ==========================================
# FOOTER
# ==========================================

footer()