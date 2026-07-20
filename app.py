from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

model = joblib.load("models/loan_default_model.joblib")

label_encoders = joblib.load("models/label_encoders.joblib")

app = FastAPI(
    title="Loan Default Prediction API"
)

class LoanInput(BaseModel):
    Age: int
    Income: float
    LoanAmount: float
    CreditScore: intpython app.py
    MonthsEmployed: int
    NumCreditLines: int
    InterestRate: float
    LoanTerm: int
    DTIRatio: float
    Education: str
    EmploymentType: str
    MaritalStatus: str
    HasMortgage: str
    HasDependents: str
    LoanPurpose: str
    HasCoSigner: str
@app.get("/")
def home():
    return {
        "message": "Welcome to the Loan Default Prediction API!"
    }
@app.post("/predict")
def predict(data: LoanInput):

    input_data = data.dict()

    for column in label_encoders:
        if column == "LoanID":
            continue
        input_data[column] = label_encoders[column].transform(
            [input_data[column]]
        )[0]

    input_df = pd.DataFrame([input_data])

    prediction = model.predict(input_df)[0]

    if prediction == 1:
        result = "Loan likely to default"
    else:
        result = "Loan not likely to default"

    return {
        "prediction": int(prediction),
        "result": result
    }