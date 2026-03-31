import streamlit as st
import pandas as pd
from database import get_connection

def equipment_management():
    st.title("🛠️ Equipment Management")
    
    tab1, tab2 = st.tabs(["View Equipment", "Add New Device"])
    
    with tab1:
        st.subheader("Inventory List")
        conn = get_connection()
        df = pd.read_sql_query("SELECT * FROM equipment", conn)
        conn.close()
        
        if not df.empty:
            st.dataframe(df, use_container_width=True)
            
            # Edit functionality
            device_to_edit = st.selectbox("Select Device to Edit", df['id'].tolist(), format_func=lambda x: f"ID {x}: {df[df['id']==x]['device_name'].values[0]}")
            
            if device_to_edit:
                device_data = df[df['id'] == device_to_edit].iloc[0]
                with st.form(f"edit_form_{device_to_edit}"):
                    new_name = st.text_input("Device Name", value=device_data['device_name'])
                    new_model = st.text_input("Model Number", value=device_data['model_number'])
                    new_dept = st.text_input("Department", value=device_data['department'])
                    new_date = st.date_input("Purchase Date", value=pd.to_datetime(device_data['purchase_date']))
                    
                    if st.form_submit_button("Update Device"):
                        conn = get_connection()
                        cursor = conn.cursor()
                        cursor.execute('''
                            UPDATE equipment 
                            SET device_name=?, model_number=?, department=?, purchase_date=?
                            WHERE id=?
                        ''', (new_name, new_model, new_dept, str(new_date), device_to_edit))
                        conn.commit()
                        conn.close()
                        st.success("Device updated!")
                        st.rerun()
        else:
            st.info("No equipment found. Add some in the next tab.")

    with tab2:
        st.subheader("Register New Equipment")
        with st.form("add_device_form"):
            name = st.text_input("Device Name")
            model = st.text_input("Model Number")
            dept = st.text_input("Department")
            p_date = st.date_input("Purchase Date")
            
            if st.form_submit_button("Add Device"):
                if name:
                    conn = get_connection()
                    cursor = conn.cursor()
                    cursor.execute('''
                        INSERT INTO equipment (device_name, model_number, department, purchase_date)
                        VALUES (?, ?, ?, ?)
                    ''', (name, model, dept, str(p_date)))
                    conn.commit()
                    conn.close()
                    st.success(f"Added {name} successfully!")
                    st.rerun()
                else:
                    st.error("Device Name is required.")
