import streamlit as st

# ==========================================
# CHECK LOGIN STATUS
# ==========================================

def check_login():
    """
    Returns True if the user is logged in.
    Initializes session variables if they don't exist.
    """

    defaults = {
        "logged_in": False,
        "user_id": None,
        "full_name": "",
        "email": ""
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value

    return st.session_state.logged_in


# ==========================================
# LOGIN USER
# ==========================================

def login_user(user_id, full_name, email):
    """
    Save user details after successful login.
    """

    st.session_state.logged_in = True
    st.session_state.user_id = user_id
    st.session_state.full_name = full_name
    st.session_state.email = email


# ==========================================
# LOGOUT USER
# ==========================================

def logout():
    """
    Clear login session and return to login page.
    """

    st.session_state.clear()

    st.rerun()
    st.switch_page("MediLink_AI.py")