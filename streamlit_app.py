import requests
import streamlit as st

st.set_page_config(page_title="Loan Default Prediction", page_icon="🏦")

st.title("🏦 Loan Default Prediction")
st.write("Enter the applicant details below.")

age = st.number_input("Age", min_value=18, max_value=100, value=35)
income = st.number_input("Annual Income", min_value=0.0, value=50000.0)
loan_amount = st.number_input("Loan Amount", min_value=0.0, value=100000.0)
credit_score = st.number_input("Credit Score", min_value=300, max_value=850, value=650)
months_employed = st.number_input("Months Employed", min_value=0, value=60)
num_credit_lines = st.number_input("Number of Credit Lines", min_value=0, value=3)
interest_rate = st.number_input("Interest Rate (%)", min_value=0.0, value=8.5)
loan_term = st.number_input("Loan Term (Months)", min_value=1, value=360)
dti_ratio = st.number_input("DTI Ratio", min_value=0.0, max_value=1.0, value=0.30)

education = st.selectbox(
    "Education",
    ["High School", "Bachelor", "Master", "PhD"]
)

employment = st.selectbox(
    "Employment Type",
    ["Full-time", "Part-time", "Self-employed", "Unemployed"]
)

marital = st.selectbox(
    "Marital Status",
    ["Single", "Married", "Divorced"]
)

mortgage = st.selectbox(
    "Has Mortgage?",
    ["Yes", "No"]
)

dependents = st.selectbox(
    "Has Dependents?",
    ["Yes", "No"]
)

purpose = st.selectbox(
    "Loan Purpose",
    ["Home", "Auto", "Business", "Education", "Other"]
)

cosigner = st.selectbox(
    "Has Co-Signer?",
    ["Yes", "No"]
)

if st.button("🔮 Predict Loan Risk"):

    data = {
        "Age": age,
        "Income": income,
        "LoanAmount": loan_amount,
        "CreditScore": credit_score,
        "MonthsEmployed": months_employed,
        "NumCreditLines": num_credit_lines,
        "InterestRate": interest_rate,
        "LoanTerm": loan_term,
        "DTIRatio": dti_ratio,
        "Education": education,
        "EmploymentType": employment,
        "MaritalStatus": marital,
        "HasMortgage": mortgage,
        "HasDependents": dependents,
        "LoanPurpose": purpose,
        "HasCoSigner": cosigner
    }

    response = requests.post(
        "https://loan-default-risk-analysis.onrender.com/predict",
        json=data
    )

    if response.status_code == 200:
        result = response.json()

        if result["prediction"] == 1:
            st.error("⚠️ Loan Likely to Default")
        else:
            st.success("✅ Loan Not Likely to Default")

        st.write(result)

    else:
        st.error("Something went wrong.")
        st.write(response.text)