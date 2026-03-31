import streamlit as st
import json
from datetime import datetime
from database import get_connection

CHECKLIST_ITEMS = [
    "Power supply check",
    "Calibration status",
    "Physical condition",
    "Display working",
    "Alarm system"
]

def inspection_module():
    st.title("📋 New Inspection")
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, device_name, model_number FROM equipment")
    devices = cursor.fetchall()
    conn.close()
    
    if not devices:
        st.warning("Please add a device in Equipment Management first.")
        return

    device_options = {f"{d[1]} (ID: {d[0]})": d[0] for d in devices}
    selected_device_name = st.selectbox("Select Device", list(device_options.keys()))
    device_id = device_options[selected_device_name]
    
    st.divider()
    
    with st.form("inspection_form"):
        results = {}
        cols = st.columns(2)
        
        for i, item in enumerate(CHECKLIST_ITEMS):
            with cols[i % 2]:
                results[item] = st.selectbox(f"{item}", ["Pass", "Fail", "Not Tested"], key=item)
        
        st.divider()
        remarks = st.text_area("Remarks")
        inspected_by = st.text_input("Inspected By")
        date = st.date_input("Inspection Date", value=datetime.now())
        
        if st.form_submit_button("Submit Inspection"):
            if inspected_by:
                conn = get_connection()
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT INTO inspections (device_id, checklist_data, remarks, inspected_by, date)
                    VALUES (?, ?, ?, ?, ?)
                ''', (device_id, json.dumps(results), remarks, inspected_by, str(date)))
                conn.commit()
                conn.close()
                st.success("Inspection recorded successfully!")
            else:
                st.error("Please enter the inspector's name.")
