import streamlit as st


def show_navigation():

    # ==========================================
    # CUSTOM CSS
    # ==========================================

    st.markdown("""
    <style>

    /* Hide Streamlit Sidebar */

    [data-testid="stSidebar"]{
        display:none;
    }

    [data-testid="stSidebarCollapsedControl"]{
        display:none;
    }

    section.main{
        margin-left:0rem;
    }

    /* Header */

    .title{
        text-align:center;
        color:#1565C0;
        font-size:34px;
        font-weight:700;
        margin-bottom:5px;
    }

    .subtitle{
        text-align:center;
        color:#666666;
        font-size:18px;
        margin-bottom:25px;
    }

    /* Buttons */

    div.stButton > button{

        height:60px;

        width:100%;

        border-radius:12px;

        border:none;

        background:#1565C0;

        color:white;

        font-size:16px;

        font-weight:600;

        transition:0.3s;

        box-shadow:0 2px 8px rgba(0,0,0,.12);

        margin-bottom:10px;

    }

    div.stButton > button:hover{

        background:#2E7D32;

        color:white;

        transform:translateY(-3px);

        box-shadow:0 8px 18px rgba(0,0,0,.20);

    }

    </style>
    """, unsafe_allow_html=True)

    # ==========================================
    # HEADER
    # ==========================================

    left, right = st.columns([6,1])

    with left:

        st.markdown(
            "<div class='title'>🏥 MediLink AI</div>",
            unsafe_allow_html=True
        )

        st.markdown(
            f"<div class='subtitle'>Welcome <b>{st.session_state.get('full_name','User')}</b> 👋</div>",
            unsafe_allow_html=True
        )

    with right:

        st.write("")

        if st.button("🚪 Logout", use_container_width=True):

            st.session_state.clear()

            st.switch_page("MediLink_AI.py")

    st.divider()

    # ==========================================
    # ROW 1
    # ==========================================

    c1, c2 = st.columns(2)

    with c1:

        if st.button("🏠\n\nHome", use_container_width=True):
            st.switch_page("pages/1_Home.py")

    with c2:

        if st.button("🤖\n\nAI Checker", use_container_width=True):
            st.switch_page("pages/2_Symptom_Checker.py")

    # ==========================================
    # ROW 2
    # ==========================================

    c3, c4 = st.columns(2)

    with c3:

        if st.button("📚\n\nHealth Education", use_container_width=True):
            st.switch_page("pages/3_Health_Education.py")

    with c4:

        if st.button("💊\n\nMedication", use_container_width=True):
            st.switch_page("pages/4_Medication_Reminder.py")

    # ==========================================
    # ROW 3
    # ==========================================

    c5, c6 = st.columns(2)

    with c5:

        if st.button("📊\n\nDashboard", use_container_width=True):
            st.switch_page("pages/5_Dashboard.py")

    with c6:

        if st.button("🚑\n\nEmergency", use_container_width=True):
            st.switch_page("pages/7_Emergency_Hospitals.py")

    # ==========================================
    # ROW 4
    # ==========================================

    c7, c8 = st.columns(2)

    with c7:

        if st.button("👤\n\nMy Profile", use_container_width=True):
            st.switch_page("pages/8_My_Profile.py")

    with c8:

        if st.button("ℹ️\n\nAbout", use_container_width=True):
            st.switch_page("pages/6_About.py")

    st.divider()