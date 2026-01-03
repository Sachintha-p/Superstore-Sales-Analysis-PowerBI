# 🚀 Superstore Sales Analysis & AI Forecasting

![Project Banner](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge) ![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python) ![PowerBI](https://img.shields.io/badge/Power%20BI-Desktop-yellow?style=for-the-badge&logo=powerbi) ![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Docker-336791?style=for-the-badge&logo=postgresql)

## 📖 Overview
This project is an **End-to-End Business Intelligence & Data Science solution** designed to analyze historical sales data and predict future trends. 

Going beyond traditional dashboards, this system integrates a **Dockerized PostgreSQL database** for data warehousing, **Power BI** for interactive visualization, and a custom **Python Machine Learning module** to forecast next month's sales figures.

---

## 🏗️ Architecture & Tech Stack

| Component | Technology Used | Description |
|-----------|----------------|-------------|
| **Database** | PostgreSQL (Docker) | Hosted the Superstore dataset in a containerized environment. |
| **ETL & Logic** | Python (Pandas, SQLAlchemy) | Extracted data from SQL, cleaned date formats, and handled missing values. |
| **Machine Learning** | Scikit-Learn | Trained a **Linear Regression** model to predict future sales based on historical trends. |
| **Visualization** | Power BI | Created an interactive dashboard with Year-over-Year (YoY) growth analysis. |

---

## 🔮 Key Features

* **Dockerized Environment:** The database runs on a Docker container, ensuring portability and isolation.
* **Automated Data Extraction:** Python scripts connect directly to the SQL database using `SQLAlchemy`.
* **Advanced Data Cleaning:** Handles `NaT` (Not a Time) errors and formats date strings (`YYYY-MM-DD`) automatically.
* **AI Forecasting:** Predicts the next month's total sales revenue using Linear Regression.
* **Interactive Dashboard:** A Power BI report connected to the database via DirectQuery/Import mode.

---

## 📸 Screenshots

### 1. AI Forecasting Output (Python)
*(Running the `ai_forecast.py` script to predict future sales)*

![Forecast Result](forecast_output.png) 

### 2. Power BI Dashboard
*(Interactive sales overview)*

![Dashboard](dashboard-final.png)

---

## 🛠️ How to Run This Project

### Prerequisites
* Docker Desktop installed
* Python 3.x installed
* Power BI Desktop

### Step 1: Database Setup
Ensure your Docker container is running:
```bash
docker start sales_db
pip install -r requirements.txt
python ai_forecast.py

Expected Output:

 Connecting to Database...
 Raw Data Loaded! Records: 9994
 AI Model Trained Successfully!
========================================
 Forecast for Next Month: $69,910.03
========================================

Sachintha Praneeth Undergraduate at SLIIT
