import sqlite3
import json
import os

DB_PATH = "data/app.db"

def init_db():
    if not os.path.exists("data"):
        os.makedirs("data")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Equipment table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS equipment (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_name TEXT NOT NULL,
            model_number TEXT,
            department TEXT,
            purchase_date DATE
        )
    ''')
    
    # Inspections table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS inspections (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id INTEGER,
            checklist_data TEXT,
            remarks TEXT,
            inspected_by TEXT,
            date DATE,
            FOREIGN KEY (device_id) REFERENCES equipment (id)
        )
    ''')
    
    conn.commit()
    conn.close()

def get_connection():
    return sqlite3.connect(DB_PATH)
