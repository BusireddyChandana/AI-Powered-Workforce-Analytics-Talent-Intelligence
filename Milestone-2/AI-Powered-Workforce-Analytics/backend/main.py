from fastapi import FastAPI
from backend.schemas import EmployeeData
from backend.model_loader import model, scaler, features
import pandas as pd


app = FastAPI(
    title="AI Workforce Analytics API",
    description="Employee Attrition Prediction API"
)



@app.get("/")
def home():

    return {
        "message": "AI Workforce Analytics Backend Running"
    }




@app.post("/predict-attrition")
def predict_attrition(data: EmployeeData):


    # Convert input into dataframe

    input_data = pd.DataFrame(
        [data.dict()]
    )


    # Add missing model features

    for feature in features:

        if feature not in input_data.columns:

            input_data[feature] = 0



    # Arrange columns according to trained model

    input_data = input_data[features]



    # Scaling

    scaled_data = scaler.transform(
        input_data
    )



    # Prediction

    probability = model.predict_proba(
        scaled_data
    )[0][1]



    probability_percentage = round(
        float(probability * 100),
        2
    )



    # Risk level

    if probability < 0.3:

        risk = "Low Risk"


    elif probability < 0.6:

        risk = "Medium Risk"


    else:

        risk = "High Risk"




    # ---------------- Health Score ----------------


    health_score = 100


    risk_factors = []



    if data.JobSatisfaction <= 2:

        health_score -= 20

        risk_factors.append(
            "Low job satisfaction"
        )



    if data.EnvironmentSatisfaction <= 2:

        health_score -= 15

        risk_factors.append(
            "Poor work environment satisfaction"
        )



    if data.JobInvolvement <= 2:

        health_score -= 15

        risk_factors.append(
            "Low job involvement"
        )



    if data.OverTime_Yes == 1:

        health_score -= 20

        risk_factors.append(
            "High overtime workload"
        )



    health_score = max(
        health_score,
        0
    )




    # ---------------- AI Recommendations ----------------


    if health_score < 50:


        recommendations = [

            "Conduct manager discussion",

            "Reduce workload pressure",

            "Provide career growth opportunities",

            "Improve workplace engagement"

        ]



    elif health_score < 75:


        recommendations = [

            "Schedule regular feedback sessions",

            "Improve job satisfaction",

            "Encourage skill development"

        ]



    else:


        recommendations = [

            "Continue employee recognition",

            "Provide growth opportunities"

        ]




    return {


        "Attrition Probability":
            probability_percentage,


        "Risk Level":
            risk,


        "Health Score":
            health_score,


        "Risk Factors":
            risk_factors,


        "Recommendations":
            recommendations

    }