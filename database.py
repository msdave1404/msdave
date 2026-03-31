import sqlite3
import json
import os

DB_PATH = "data/app.db"

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS equipment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_name TEXT NOT NULL,
            model_number TEXT,
            department TEXT,
            purchase_date DATE,
            manufacturer TEXT,
            operating_voltage TEXT,
            battery_spec TEXT,
            checklist_fields TEXT
        )
    ''')

    # Seed Default Data if table is empty
    cursor.execute("SELECT COUNT(*) FROM equipment")
    if cursor.fetchone()[0] == 0:
        default_devices = [
            ("ECG Machine", "MAC-2000", "Cardiology", "2024-01-01", "GE Healthcare", "230V", "Li-ion 14.4V", '["Power-On Self Test", "Lead-Off Detection", "Baseline Stability", "Common Mode Rejection", "Heart Rate Accuracy"]'),
            ("Ventilator", "Puritan Bennett 980", "ICU", "2024-01-01", "Medtronic", "230V", "Backup Lead-Acid", '["Oxygen Supply Pressure", "Air Supply Pressure", "Exhalation Valve Test", "Safety Valve Test", "Battery Backup Test"]'),
            ("Patient Monitor", "IntelliVue MX550", "ER", "2024-01-01", "Philips", "230V", "Rechargeable Li-ion", '["Display Pixel Test", "NIBP Pump Test", "SpO2 Module Sync", "Temperature Probe Continuity", "Alarm System Audio"]')
        ]
        cursor.executemany('''
            INSERT INTO equipment (device_name, model_number, department, purchase_date, manufacturer, operating_voltage, battery_spec, checklist_fields)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', default_devices)
        
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inspections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id INTEGER,
            checklist_data TEXT,
            remarks TEXT,
            inspected_by TEXT,
            date DATE,
            serial_number TEXT,
            job_card_no TEXT,
            technician TEXT,
            visual_inspection TEXT, -- JSON
            operational_test TEXT, -- JSON
            self_test TEXT, -- JSON
            settings_check TEXT, -- JSON
            FOREIGN KEY (device_id) REFERENCES equipment (id)
        )
    ''')

    # Seed initial data from Machine.md if empty
    cursor.execute("SELECT COUNT(*) FROM equipment")
    if cursor.fetchone()[0] == 0:
        sample_devices = [
            ("Ventilator", "V-100", "ICU", "2023-01-01", "Philips", "230V", "12V, 7Ah", 
             json.dumps(["Oxygen Supply Check", "Air Supply Check", "Leak Test", "Software & Firmware Check"])),
            ("Ultrasound", "US-200", "Radiology", "2023-05-10", "GE", "230V", "N/A", 
             json.dumps(["System Boot & UI Test", "Probe Holder Board", "Image Quality Test", "DC-DC Board", "Data Storage & Connectivity", "Audio Check and keyboard test"])),
            ("Patient Monitor", "PM-50", "General Ward", "2024-02-15", "Mindray", "230V", "12V, 2.3Ah", 
             json.dumps(["System Boot & UI Test", "Data Storage & Connectivity", "ECG Test", "SpO2 Test", "NIBP Test", "Temperature Test"])),
            ("Defibrillator", "HeartStart XL", "Emergency", "2024-06-28", "Philips", "230V", "12V, 2.3Ah", 
             json.dumps(["Power supply check", "Calibration status", "Physical condition", "Display working", "Alarm system"]))
        ]
        cursor.executemany('''
            INSERT INTO equipment (device_name, model_number, department, purchase_date, manufacturer, operating_voltage, battery_spec, checklist_fields)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', sample_devices)
    
    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect(DB_PATH)
