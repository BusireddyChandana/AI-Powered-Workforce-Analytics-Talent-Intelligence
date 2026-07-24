import streamlit as st
import pandas as pd
import plotly.express as px
import requests


# ---------------- Page Settings ----------------

st.set_page_config(
    page_title="AI Workforce Analytics",
    page_icon="🤖",
    layout="wide"
)



# ---------------- Sidebar ----------------

st.sidebar.title(
    "🤖 AI Workforce Analytics"
)


st.sidebar.markdown("---")


st.sidebar.info(
    """
    **Infosys Springboard Internship**

    Milestone-2

    AI Workforce Analytics & Talent Intelligence
    """
)


st.sidebar.markdown("---")


st.sidebar.success(
    "Backend: Connected"
)



# ---------------- Dataset ----------------


@st.cache_data
def load_data():

    return pd.read_csv(
        "data/WA_Fn-UseC_-HR-Employee-Attrition.csv"
    )


df = load_data()



# ---------------- Title ----------------


st.title(
    "🤖 AI Workforce Analytics & Talent Intelligence"
)


st.write(
    "AI-powered employee analytics and attrition insights dashboard"
)



# ---------------- Workforce Overview ----------------


st.header(
    "📊 Workforce Overview"
)


total_employees = len(df)


attrition_count = (
    df["Attrition"] == "Yes"
).sum()


attrition_rate = round(
    (attrition_count / total_employees) * 100,
    2
)


avg_income = round(
    df["MonthlyIncome"].mean(),
    0
)



col1, col2, col3, col4 = st.columns(4)



col1.metric(
    "Total Employees",
    total_employees
)


col2.metric(
    "Attrition Rate",
    f"{attrition_rate}%"
)


col3.metric(
    "Average Income",
    f"${avg_income}"
)


col4.metric(
    "Departments",
    df["Department"].nunique()
)



st.divider()



# ---------------- Workforce Analytics ----------------


st.header(
    "📈 Workforce Analytics"
)



# Department Attrition


dept_attrition = (

    df.groupby("Department")["Attrition"]

    .apply(
        lambda x: (x=="Yes").sum()
    )

    .reset_index()

)



fig1 = px.bar(

    dept_attrition,

    x="Department",

    y="Attrition",

    color="Department",

    text="Attrition",

    title="Attrition by Department"

)


fig1.update_traces(
    textposition="outside"
)


st.plotly_chart(
    fig1,
    use_container_width=True
)



# Overtime Analysis


overtime_data = (

    df.groupby("OverTime")["Attrition"]

    .apply(
        lambda x:(x=="Yes").sum()
    )

    .reset_index()

)



fig2 = px.pie(

    overtime_data,

    names="OverTime",

    values="Attrition",

    title="Overtime Impact on Attrition"

)


st.plotly_chart(
    fig2,
    use_container_width=True
)



# Job Satisfaction


st.subheader(
    "⭐ Job Satisfaction Analysis"
)



satisfaction = (

    df.groupby("JobSatisfaction")["Attrition"]

    .apply(
        lambda x:(x=="Yes").sum()
    )

    .reset_index()

)



fig3 = px.bar(

    satisfaction,

    x="JobSatisfaction",

    y="Attrition",

    title="Attrition Based on Job Satisfaction"

)


st.plotly_chart(
    fig3,
    use_container_width=True
)



# Job Role Analysis


st.subheader(
    "💼 Job Role Attrition Analysis"
)



role_attrition = (

    df.groupby("JobRole")["Attrition"]

    .apply(
        lambda x:(x=="Yes").sum()
    )

    .reset_index()

)



fig4 = px.bar(

    role_attrition,

    x="JobRole",

    y="Attrition",

    color="JobRole",

    text="Attrition",

    title="Attrition by Job Role"

)



fig4.update_traces(
    textposition="outside"
)



st.plotly_chart(
    fig4,
    use_container_width=True
)
# ---------------- Age Analysis ----------------


st.subheader(
    "👥 Age Group Attrition Analysis"
)


age_attrition = (

    df.groupby("Age")["Attrition"]

    .apply(
        lambda x:(x=="Yes").sum()
    )

    .reset_index()

)


fig5 = px.line(

    age_attrition,

    x="Age",

    y="Attrition",

    markers=True,

    title="Attrition Trend by Age"

)


st.plotly_chart(
    fig5,
    use_container_width=True
)




# ---------------- Income Analysis ----------------


st.subheader(
    "💰 Income Analysis"
)


fig6 = px.box(

    df,

    x="Attrition",

    y="MonthlyIncome",

    title="Monthly Income vs Attrition"

)


st.plotly_chart(
    fig6,

    use_container_width=True
)




# ---------------- Workforce Risk Distribution ----------------


st.divider()


st.header(
    "⚠️ Workforce Risk Distribution"
)



risk_data = pd.DataFrame({

    "Risk Level":[
        "High Risk",
        "Medium Risk",
        "Low Risk"
    ],


    "Employees":[

        int(
            (df["Attrition"]=="Yes").sum()
        ),

        int(
            len(df)*0.25
        ),

        int(
            len(df)
            -
            (df["Attrition"]=="Yes").sum()
            -
            (len(df)*0.25)
        )
    ]

})



fig7 = px.pie(

    risk_data,

    names="Risk Level",

    values="Employees",

    title="Employee Risk Distribution"

)



st.plotly_chart(

    fig7,

    use_container_width=True

)




# ---------------- AI Employee Risk Prediction ----------------


st.divider()


st.header(
    "🤖 AI Employee Risk Prediction"
)


st.write(
    "Enter complete employee details to predict attrition risk"
)



col1,col2,col3 = st.columns(3)



with col1:


    age = st.number_input(
        "Age",
        value=30
    )


    daily_rate = st.number_input(
        "Daily Rate",
        value=800
    )


    distance = st.number_input(
        "Distance From Home",
        value=10
    )



with col2:


    education = st.number_input(
        "Education",
        value=3
    )


    environment = st.number_input(
        "Environment Satisfaction",
        value=4
    )


    hourly_rate = st.number_input(
        "Hourly Rate",
        value=60
    )



with col3:


    job_involvement = st.number_input(
        "Job Involvement",
        value=4
    )


    job_level = st.number_input(
        "Job Level",
        value=2
    )


    job_satisfaction = st.number_input(
        "Job Satisfaction",
        value=4
    )



monthly_income = st.number_input(
    "Monthly Income",
    value=10000
)


monthly_rate = st.number_input(
    "Monthly Rate",
    value=20000
)


companies = st.number_input(
    "Number of Companies Worked",
    value=2
)


total_working_years = st.number_input(
    "Total Working Years",
    value=5
)


years_at_company = st.number_input(
    "Years At Company",
    value=3
)


years_current_role = st.number_input(
    "Years In Current Role",
    value=2
)


years_since_promotion = st.number_input(
    "Years Since Last Promotion",
    value=1
)


years_with_manager = st.number_input(
    "Years With Current Manager",
    value=2
)


training_year = st.number_input(
    "Training Times Last Year",
    value=3
)


work_life_balance = st.number_input(
    "Work Life Balance",
    value=3
)


relationship_satisfaction = st.number_input(
    "Relationship Satisfaction",
    value=3
)


stock_option = st.number_input(
    "Stock Option Level",
    value=1
)


performance_rating = st.number_input(
    "Performance Rating",
    value=3
)



business_travel = st.selectbox(

    "Business Travel",

    [
        "Travel_Rarely",
        "Travel_Frequently"
    ]

)


department = st.selectbox(

    "Department",

    [
        "Research & Development",
        "Sales"
    ]

)


gender = st.selectbox(

    "Gender",

    [
        "Male",
        "Female"
    ]

)


marital_status = st.selectbox(

    "Marital Status",

    [
        "Single",
        "Married"
    ]

)


job_role = st.selectbox(

    "Job Role",

    [
        "Sales Executive",
        "Research Scientist",
        "Laboratory Technician",
        "Manager"
    ]

)


education_field = st.selectbox(

    "Education Field",

    [
        "Life Sciences",
        "Marketing",
        "Medical",
        "Other",
        "Technical Degree"
    ]

)


overtime = st.selectbox(

    "OverTime",

    [
        "No",
        "Yes"
    ]

)
# ---------------- Prediction ----------------


if st.button(
    "🔍 Predict Attrition Risk"
):


    payload = {

        "Age": age,
        "DailyRate": daily_rate,
        "DistanceFromHome": distance,
        "Education": education,
        "EnvironmentSatisfaction": environment,
        "HourlyRate": hourly_rate,
        "JobInvolvement": job_involvement,
        "JobLevel": job_level,
        "JobSatisfaction": job_satisfaction,

        "MonthlyIncome": monthly_income,
        "MonthlyRate": monthly_rate,

        "NumCompaniesWorked": companies,

        "PercentSalaryHike": 15,
        "PerformanceRating": performance_rating,

        "RelationshipSatisfaction": relationship_satisfaction,

        "StockOptionLevel": stock_option,

        "TotalWorkingYears": total_working_years,

        "TrainingTimesLastYear": training_year,

        "WorkLifeBalance": work_life_balance,

        "YearsAtCompany": years_at_company,

        "YearsInCurrentRole": years_current_role,

        "YearsSinceLastPromotion": years_since_promotion,

        "YearsWithCurrManager": years_with_manager,


        "BusinessTravel_Travel_Frequently":
            1 if business_travel=="Travel_Frequently" else 0,

        "BusinessTravel_Travel_Rarely":
            1 if business_travel=="Travel_Rarely" else 0,


        "Department_Research_Development":
            1 if department=="Research & Development" else 0,

        "Department_Sales":
            1 if department=="Sales" else 0,


        "EducationField_Life_Sciences":
            1 if education_field=="Life Sciences" else 0,

        "EducationField_Marketing":
            1 if education_field=="Marketing" else 0,

        "EducationField_Medical":
            1 if education_field=="Medical" else 0,

        "EducationField_Other":
            1 if education_field=="Other" else 0,

        "EducationField_Technical_Degree":
            1 if education_field=="Technical Degree" else 0,


        "Gender_Male":
            1 if gender=="Male" else 0,


        "JobRole_Human_Resources":0,

        "JobRole_Laboratory_Technician":
            1 if job_role=="Laboratory Technician" else 0,

        "JobRole_Manager":
            1 if job_role=="Manager" else 0,

        "JobRole_Manufacturing_Director":0,

        "JobRole_Research_Director":0,

        "JobRole_Research_Scientist":
            1 if job_role=="Research Scientist" else 0,

        "JobRole_Sales_Executive":
            1 if job_role=="Sales Executive" else 0,

        "JobRole_Sales_Representative":0,


        "MaritalStatus_Married":
            1 if marital_status=="Married" else 0,

        "MaritalStatus_Single":
            1 if marital_status=="Single" else 0,


        "OverTime_Yes":
            1 if overtime=="Yes" else 0
    }



    try:


        response = requests.post(

            "http://127.0.0.1:8000/predict-attrition",

            json=payload

        )


        result = response.json()



        st.success(
            "Prediction Completed"
        )


        c1,c2 = st.columns(2)


        c1.metric(

            "Attrition Probability",

            f"{result['Attrition Probability']}%"

        )



        c2.metric(

            "Risk Level",

            result["Risk Level"]

        )

        
                # ---------------- Employee Health Score ----------------

        health_score = 100

        risk_factors = []


        if job_satisfaction <= 2:

            health_score -= 20

            risk_factors.append(
                "Low job satisfaction"
            )


        if environment <= 2:

            health_score -= 15

            risk_factors.append(
                "Poor work environment satisfaction"
            )


        if job_involvement <= 2:

            health_score -= 15

            risk_factors.append(
                "Low employee involvement"
            )


        if overtime == "Yes":

            health_score -= 20

            risk_factors.append(
                "High overtime workload"
            )


        prediction_probability = result["Attrition Probability"]


        if prediction_probability >= 60:

            health_score -= 25

            risk_factors.append(
                "AI model predicts high attrition probability"
            )


        elif prediction_probability >= 30:

            health_score -= 10

            risk_factors.append(
                "Moderate attrition probability"
            )


        health_score = max(
            health_score,
            0
        )


        st.subheader(
            "🩺 Employee Health Score"
        )


        st.metric(
            "Health Score",
            f"{health_score}/100"
        )


        st.subheader(
            "⚠️ Key Risk Factors"
        )


        if risk_factors:

            for item in risk_factors:

                st.warning(item)

        else:

            st.success(
                "No major risk factors detected"
            )


        st.subheader(
            "🤖 AI Recommendations"
        )


        if health_score < 50:

            recommendations = [
                "Conduct manager discussion",
                "Reduce workload pressure",
                "Provide career growth opportunities"
            ]

        elif health_score < 75:

            recommendations = [
                "Schedule feedback sessions",
                "Improve job satisfaction",
                "Encourage skill development"
            ]

        else:

            recommendations = [
                "Continue employee recognition",
                "Provide growth opportunities"
            ]


        for item in recommendations:

            st.write(
                "- " + item
            )
    except Exception as e:


        st.error(
            f"Backend connection failed: {e}"
        )




# ---------------- HR Analytics Assistant ----------------


st.divider()


st.subheader(
    "💬 HR Analytics Assistant"
)



question = st.text_input(
    "Ask your HR question:"
)



if st.button(
    "Ask Assistant"
):


    q = question.lower()



    if "highest attrition" in q:


        result = (

            df.groupby("Department")["Attrition"]

            .apply(
                lambda x:(x=="Yes").sum()
            )

        )


        st.success(

            f"{result.idxmax()} department has highest attrition with {result.max()} employees leaving."

        )



    elif "attrition rate" in q:


        st.success(

            f"Overall attrition rate is {attrition_rate}%."

        )



    elif "total employees" in q:


        st.success(

            f"Total employees: {total_employees}"

        )



    elif "average income" in q:


        st.success(

            f"Average income: ${avg_income}"

        )



    elif "job role" in q:


        role = (

            df.groupby("JobRole")["Attrition"]

            .apply(
                lambda x:(x=="Yes").sum()
            )

        )


        st.success(

            f"{role.idxmax()} role has highest attrition."

        )



    else:


        st.info(
            """
            Try asking:

            - highest attrition
            - attrition rate
            - total employees
            - average income
            - job role
            """
        )