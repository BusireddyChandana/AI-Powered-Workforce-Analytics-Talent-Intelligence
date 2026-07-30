import plotly.express as px


def department_chart(df):
    """
    Department-wise headcount chart
    """

    dept_count = df["Department"].value_counts().reset_index()

    dept_count.columns = ["Department", "Employees"]

    fig = px.bar(
        dept_count,
        x="Department",
        y="Employees",
        title="Department Wise Headcount"
    )

    return fig


def gender_chart(df):
    """
    Diversity metric - Gender distribution
    """

    gender_count = df["Gender"].value_counts().reset_index()

    gender_count.columns = ["Gender", "Count"]

    fig = px.pie(
        gender_count,
        names="Gender",
        values="Count",
        title="Gender Diversity"
    )

    return fig


def age_distribution_chart(df):
    """
    Employee age distribution
    """

    fig = px.histogram(
        df,
        x="Age",
        title="Employee Age Distribution",
        nbins=20
    )

    return fig


def satisfaction_chart(df):
    """
    Employee engagement trend
    """

    satisfaction = (
        df.groupby("JobSatisfaction")
        .size()
        .reset_index(name="Employees")
    )

    fig = px.line(
        satisfaction,
        x="JobSatisfaction",
        y="Employees",
        title="Employee Job Satisfaction Trend"
    )

    return fig