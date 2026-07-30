import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

import streamlit as st

from components import (
    load_data,
    get_kpi_metrics
)

from charts import (
    department_chart,
    gender_chart,
    age_distribution_chart,
    satisfaction_chart
)

from reports.generate_report import create_report
from auth.login import login, check_role


# Page configuration
st.set_page_config(
    page_title="AI Workforce Intelligence Dashboard",
    page_icon="🤖",
    layout="wide"
)


# Role Based Login
login()

user_role = check_role()


if user_role:

    st.sidebar.info(
        f"Current Role: {user_role}"
    )

else:

    st.warning(
        "Please login from the sidebar to access workforce intelligence dashboard."
    )

    st.stop()


# Dashboard Title
st.title("🤖 AI Workforce Intelligence Dashboard")

st.markdown(
    "Interactive analytics dashboard for workforce insights and talent intelligence"
)


# Load workforce data
df = load_data()


# KPI Metrics
kpis = get_kpi_metrics(df)


st.subheader("📊 Workforce Overview")


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Total Employees",
        kpis["Total Employees"]
    )


with col2:
    st.metric(
        "Attrition Rate",
        f'{kpis["Attrition Rate"]}%'
    )


with col3:
    st.metric(
        "Average Income",
        f'${kpis["Average Income"]}'
    )


with col4:
    st.metric(
        "Departments",
        kpis["Departments"]
    )


st.divider()


# Headcount Analytics

st.subheader("🏢 Headcount Analytics")

st.plotly_chart(
    department_chart(df),
    use_container_width=True
)


# Diversity Metrics

st.subheader("🌍 Diversity Metrics")


col1, col2 = st.columns(2)


with col1:

    st.plotly_chart(
        gender_chart(df),
        use_container_width=True
    )


with col2:

    st.plotly_chart(
        age_distribution_chart(df),
        use_container_width=True
    )


# Engagement Trends

st.subheader("😊 Employee Engagement Trends")


st.plotly_chart(
    satisfaction_chart(df),
    use_container_width=True
)


# Dataset Preview

with st.expander("View Employee Data"):

    st.dataframe(
        df.head(20)
    )


# Executive Report Generation

st.divider()


st.subheader(
    "📄 Executive Talent Intelligence Report"
)


if st.button("Generate Executive Report"):

    report_file = create_report(df)


    with open(report_file, "r", encoding="utf-8") as file:

        report_text = file.read()


    st.success(
        "Executive report generated successfully!"
    )


    st.download_button(
        label="Download Report",
        data=report_text,
        file_name="executive_workforce_report.txt",
        mime="text/plain"
    )