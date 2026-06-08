# 🌩️ Storm Prediction Dashboard

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
  <img src="https://img.shields.io/badge/Bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white"/>
</p>

> **Solartis Hackathon Contest** · Dec 2020 – Jan 2021  
> Real-time geospatial storm risk analysis tool for insurance underwriting decisions.

---

## 🎯 Project Overview

Built for the **Solartis Hackathon**, this dashboard enables insurance companies to forecast impending storms and hurricanes, supporting informed business decisions about rate adjustments and regional underwriting exposure.

The system ingests geospatial storm data, visualises storm trajectories interactively on a map, and automatically delivers state-wise risk reports to relevant stakeholders via email.

---

## ✨ Key Features

**Interactive Map Visualisation**
- Storm track mapping using **Folium (Leaflet.js)**, interactive, zoomable geospatial views
- State-level risk overlays for rapid regional assessment

**Automated Reporting**
- Dynamic **PDF report generation** per state using FPDF
- Secure email delivery via **SMTP with StartTLS**, automated dispatch to underwriting teams

**Data Pipeline**
- JSON and CSV geospatial storm data ingestion
- Modular Python scripts with SQL-based data filtering
- MySQL backend for historical storm data storage and querying

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python · MySQL |
| Frontend | HTML · CSS · JavaScript · Bootstrap |
| Mapping | Folium (Leaflet.js) |
| Reporting | FPDF (dynamic PDF generation) |
| Email | SMTP + StartTLS |
| Data | JSON · CSV ingestion |

---

## 🗂️ Repository Structure

```
Storm-Prediction-Dashboard/
├── app.py                          # Main Flask application
├── storm_analysis.py               # Core prediction logic
├── report_generator.py             # FPDF-based PDF reports
├── email_sender.py                 # SMTP email automation
├── static/
│   ├── css/
│   └── js/
├── templates/
│   └── dashboard.html              # Folium map + UI
├── data/
│   ├── storm_data.json
│   └── storm_data.csv
├── storm prediction dashboard.pdf  # Project documentation
├── STORM PREDICTION DASHBOARD output.pdf
└── README.md
```

---

## 👩‍💻 Author

**Ramya Subramanian Porselva Bharathi**  
[LinkedIn](https://www.linkedin.com/in/ramya_sp) · [GitHub](https://github.com/ramyasp64)
