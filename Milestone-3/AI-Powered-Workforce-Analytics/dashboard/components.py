import pandas as pd


def load_data():
    """
    Load workforce dataset
    """
    file_path = "../data/WA_Fn-UseC_-HR-Employee-Attrition.csv"

    df = pd.read_csv(file_path)

    return df


def get_kpi_metrics(df):
    """
    Calculate dashboard KPI metrics
    """

    total_employees = len(df)

    attrition_rate = (
        (df["Attrition"] == "Yes").sum() / total_employees
    ) * 100

    avg_income = df["MonthlyIncome"].mean()

    departments = df["Department"].nunique()

    return {
        "Total Employees": total_employees,
        "Attrition Rate": round(attrition_rate, 2),
        "Average Income": round(avg_income, 2),
        "Departments": departments
    }


def get_attrition_count(df):
    """
    Attrition distribution
    """

    return df["Attrition"].value_counts()


def get_department_count(df):
    """
    Department employee distribution
    """

    return df["Department"].value_counts()