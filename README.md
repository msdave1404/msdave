# 🏥 Biomedical Equipment Inspection System (BEIS)

**BEIS** is a specialized web-based management platform designed for biomedical engineers and students to maintain hospital inventory and document device safety and performance through professional inspection reports.

## 🚀 Key Features

*   **🔒 Secure Access**: Simplified administrative dashboard with session management.
*   **📂 Equipment Inventory**: Comprehensive lifecycle tracking (Device Specs, Dept, Manufacturer, Voltage/Battery Specs).
*   **📋 Dynamic Inspection Workflows**:
    *   Template-based checklists per device type (Ventilators, Monitors, etc.).
    *   **Unit-Level Customization**: Add or remove specific tests on-the-fly for unique units.
*   **📜 History & Analytics**: Full audit trail of past inspections with "Device Health Score" calculations.
*   **📄 Professional PDF Reporting**: Generates industry-standard job cards (including Serial No, Job Card IDs, and Technician sign-offs) using WeasyPrint.
*   **🐳 Production Ready**: Fully containerized with Docker and Docker Compose for easy deployment.

## 🛠️ Tech Stack

*   **Frontend/Backend**: [Streamlit](https://streamlit.io/) (Python)
*   **Database**: SQLite (Local & Persistent)
*   **PDF Engine**: WeasyPrint & Jinja2 Templates
*   **Infrastructure**: Docker

## 📥 Installation & Running

### Option 1: Using Docker (Recommended)
```bash
docker-compose up --build
```
Access at: `http://localhost:8501`

### Option 2: Local Installation
1. Install Python 3.10+
2. Install system dependencies for WeasyPrint (e.g., `brew install pango` on macOS)
3. `pip install -r requirements.txt`
4. `streamlit run app.py`

## 👤 Credentials
*   **Username**: `admin`
*   **Password**: `biomed2024`
