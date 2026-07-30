# AI-Powered Workforce Analytics & Talent Intelligence

## Milestone-3: Workforce Intelligence Dashboard

## Overview

This milestone focuses on integrating the AI analytics engine with an interactive workforce intelligence dashboard. The system provides workforce insights, visualization modules, executive reports, and role-based access for HR stakeholders.

## Features

### 1. Interactive Workforce Dashboard

- Employee workforce overview
- Total employee count
- Attrition rate analysis
- Average income analysis
- Department insights


### 2. Visualization Modules

- Department-wise headcount analytics
- Gender diversity analysis
- Employee age distribution
- Job satisfaction and engagement trends


### 3. Executive Talent Intelligence Reports

- Automated workforce summary generation
- Attrition insights
- Strategic HR recommendations
- Downloadable executive reports


### 4. Role-Based Access Control

Available roles:

- HR Admin
  - Complete dashboard access
  - Generate executive reports

- Manager
  - Workforce insights access

- Employee
  - Basic workforce information access


## Project Structure

```text
AI-Powered-Workforce-Analytics
│
├── dashboard
│   ├── app.py
│   ├── charts.py
│   └── components.py
│
├── backend
│   └── api_connection.py
│
├── models
│   ├── attrition_model.pkl
│   ├── scaler.pkl
│   └── features.pkl
│
├── data
│   └── WA_Fn-UseC_-HR-Employee-Attrition.csv
│
├── reports
│   ├── executive_summary.py
│   └── generate_report.py
│
├── auth
│   └── login.py
│
├── tests
├── docs
├── README.md
└── requirements.txt
Technologies Used
Python
Streamlit
Pandas
NumPy
Plotly
Scikit-learn
Machine Learning
FastAPI
How to Run

Install dependencies:

pip install -r requirements.txt

Run dashboard:

python -m streamlit run dashboard/app.py
Demo Login Credentials
HR Admin

Username:

hr_admin

Password:

admin123
Dataset

IBM HR Analytics Employee Attrition & Performance Dataset

Outcome

The system enables organizations to monitor workforce trends, identify employee risks, generate strategic reports, and support data-driven HR decisions.

The AI-powered dashboard provides workforce intelligence through analytics, visualization, reporting, and role-based collaboration features.


