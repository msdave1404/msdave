import streamlit as st
from database import init_db
from modules.auth import login_page, logout
from modules.equipment import equipment_management
from modules.manual_inspection import inspection_module as manual_inspection
from modules.automated_inspection import automated_inspection
from modules.history import inspection_history

# Initialize DB on start
init_db()

st.set_page_config(page_title="Biomed-Inspection System", page_icon="🏥", layout="wide")

# Session state for auth
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_page()
else:
    # Sidebar Navigation
    st.sidebar.title("🏥 Biomed-Inspect")
    st.sidebar.write("Navigate through modules")
    
    page = st.sidebar.radio("Go to", 
        ["Equipment Management", "Manual Inspection", "Automated Testing", "Inspection History"]
    )
    
    st.sidebar.divider()
    if st.sidebar.button("Logout"):
        logout()

    # Page Routing
    if page == "Equipment Management":
        equipment_management()
    elif page == "Manual Inspection":
        manual_inspection()
    elif page == "Automated Testing":
        automated_inspection()
    elif page == "Inspection History":
        inspection_history()

