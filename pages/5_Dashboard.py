import streamlit as st
from datetime import datetime

from auth.auth import check_login
from utils.navigation import show_navigation

from database.database import (
    get_total_reminders,
    get_total_ai_checks,
    get_total_users,
    get_user_profile
)

from utils.helper import (
    footer,
    section_title,
    health_tip
)

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Dashboard | MediLink AI",
    page_icon="📊",
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
# LOAD USER
# ==========================================

user = get_user_profile(st.session_state.user_id)

# ==========================================
# HERO SECTION
# ==========================================

st.markdown("""
<div class="hero">

<h1>📊 Dashboard</h1>

<h3>Your Healthcare Activity at a Glance</h3>

<p style="font-size:18px;">

Monitor your healthcare activities and quickly access MediLink AI features.

</p>

</div>
""", unsafe_allow_html=True)

# ==========================================
# WELCOME
# ==========================================

st.info(f"""
👋 **Welcome back, {st.session_state.full_name}!**

Here's a quick overview of your MediLink AI account.
""")

# ==========================================
# ACCOUNT OVERVIEW
# ==========================================

section_title("Healthcare Overview", "📈")

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
        "👥 Users",
        get_total_users()
    )

with col4:

    days = (
    datetime.now() -
    datetime.strptime(
        user["created_at"][:10],
        "%Y-%m-%d"
    )
).days
    st.metric(
        "📅 Member For",
        f"{days} Days"
    )

st.divider()

# ==========================================
# QUICK ACTIONS
# ==========================================

section_title("Quick Actions", "🚀")

c1, c2 = st.columns(2)

with c1:

    if st.button(
        "🤖 Open AI Symptom Checker",
        use_container_width=True
    ):
        st.switch_page("pages/2_Symptom_Checker.py")

    if st.button(
        "💊 Open Medication Reminder",
        use_container_width=True
    ):
        st.switch_page("pages/4_Medication_Reminder.py")

with c2:

    if st.button(
        "📚 Open Health Education",
        use_container_width=True
    ):
        st.switch_page("pages/3_Health_Education.py")

    if st.button(
        "🚑 Emergency Hospitals",
        use_container_width=True
    ):
        st.switch_page("pages/7_Emergency_Hospitals.py")

st.divider()

# ==========================================
# ACCOUNT STATUS
# ==========================================

section_title("Account Status", "🟢")

left, right = st.columns(2)

with left:

    st.success(f"""

### 👤 Profile

**Name:** {user["full_name"]}

**Email:** {user["email"]}

**Phone:** {user["phone"]}

""")

with right:

    st.info(f"""

### 📋 Membership

**Age:** {user["age"]}

**Gender:** {user["gender"]}

**Member Since:** {user["created_at"][:10]}

""")

st.divider()

# ==========================================
# HEALTH TIP
# ==========================================

section_title("Health Tip of the Day", "💡")

health_tip()

st.divider()

# ==========================================
# WHAT YOU CAN DO
# ==========================================

section_title("What You Can Do with MediLink AI", "❤️")

st.success("""

✅ Analyze your symptoms with AI

✅ Learn about common diseases

✅ Save medication reminders

✅ Find emergency healthcare information

✅ Manage your secure healthcare profile

✅ Download AI health reports

""")

st.divider()

# ==========================================
# MEDICAL DISCLAIMER
# ==========================================

st.warning("""

### ⚠️ Medical Disclaimer

MediLink AI provides educational healthcare information only.

It does **NOT** diagnose diseases.

It does **NOT** prescribe medications.

Always consult a licensed healthcare professional for diagnosis and treatment.

""")

# ==========================================
# FOOTER
# ==========================================

footer()