from pydantic import BaseModel


class EmployeeData(BaseModel):

    Age: int
    DailyRate: int
    DistanceFromHome: int
    Education: int
    EnvironmentSatisfaction: int
    HourlyRate: int
    JobInvolvement: int
    JobLevel: int
    JobSatisfaction: int
    MonthlyIncome: int
    MonthlyRate: int
    NumCompaniesWorked: int
    PercentSalaryHike: int
    PerformanceRating: int
    RelationshipSatisfaction: int
    StockOptionLevel: int
    TotalWorkingYears: int
    TrainingTimesLastYear: int
    WorkLifeBalance: int
    YearsAtCompany: int
    YearsInCurrentRole: int
    YearsSinceLastPromotion: int
    YearsWithCurrManager: int

    BusinessTravel_Travel_Frequently: int
    BusinessTravel_Travel_Rarely: int

    Department_Research_Development: int
    Department_Sales: int

    EducationField_Life_Sciences: int
    EducationField_Marketing: int
    EducationField_Medical: int
    EducationField_Other: int
    EducationField_Technical_Degree: int

    Gender_Male: int

    JobRole_Human_Resources: int
    JobRole_Laboratory_Technician: int
    JobRole_Manager: int
    JobRole_Manufacturing_Director: int
    JobRole_Research_Director: int
    JobRole_Research_Scientist: int
    JobRole_Sales_Executive: int
    JobRole_Sales_Representative: int

    MaritalStatus_Married: int
    MaritalStatus_Single: int

    OverTime_Yes: int