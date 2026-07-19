import requests
import streamlit as st

# -----------------------------
# PAGE CONFIGURATION
# -----------------------------
st.set_page_config(
    page_title="Loan Default Prediction System",
    page_icon="🏦",
    layout="wide"
)

# -----------------------------
# HEADER
# -----------------------------
st.title("🏦 Loan Default Prediction System")

st.markdown("""
Predict whether a loan applicant is likely to default using a Machine Learning model.

**Capstone Project – AnalystLab Africa Machine Learning Internship**
""")

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("📋 Project Information")

st.sidebar.info("""
### Model
Random Forest Classifier

### Backend
FastAPI

### Frontend
Streamlit

### API Deployment
Render

### Developer
Funbi Opemipo Olowojesiku
""")

# -----------------------------
# INPUT FORM
# -----------------------------
st.header("📝 Applicant Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=35
    )

    income = st.number_input(
        "Annual Income",
        min_value=0.0,
        value=50000.0
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0.0,
        value=100000.0
    )

    credit_score = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=850,
        value=650
    )

    months_employed = st.number_input(
        "Months Employed",
        min_value=0,
        value=60
    )

with col2:

    num_credit_lines = st.number_input(
        "Number of Credit Lines",
        min_value=0,
        value=3
    )

    interest_rate = st.number_input(
        "Interest Rate (%)",
        min_value=0.0,
        value=8.5
    )

    loan_term = st.number_input(
        "Loan Term (Months)",
        min_value=1,
        value=360
    )

    dti_ratio = st.slider(
        "Debt-to-Income Ratio",
        min_value=0.0,
        max_value=1.0,
        value=0.30
    )

st.subheader("Additional Information")

col3, col4 = st.columns(2)

with col3:

    education = st.selectbox(
        "Education",
        [
            "High School",
            "Bachelor",
            "Master",
            "PhD"
        ]
    )

    employment = st.selectbox(
        "Employment Type",
        [
            "Full-time",
            "Part-time",
            "Self-employed",
            "Unemployed"
        ]
    )

    marital = st.selectbox(
        "Marital Status",
        [
            "Single",
            "Married",
            "Divorced"
        ]
    )

with col4:

    mortgage = st.selectbox(
        "Has Mortgage?",
        [
            "Yes",
            "No"
        ]
    )

    dependents = st.selectbox(
        "Has Dependents?",
        [
            "Yes",
            "No"
        ]
    )

    purpose = st.selectbox(
        "Loan Purpose",
        [
            "Home",
            "Auto",
            "Business",
            "Education",
            "Other"
        ]
    )

    cosigner = st.selectbox(
        "Has Co-Signer?",
        [
            "Yes",
            "No"
        ]
    )

# -----------------------------
# PREDICT BUTTON
# -----------------------------
if st.button("🔮 Predict Loan Risk", use_container_width=True):

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

    with st.spinner("🔍 Predicting loan risk..."):

        response = requests.post(
            "https://loan-default-risk-analysis.onrender.com/predict",
            json=data
        )

    st.divider()

    if response.status_code == 200:

        result = response.json()

        st.subheader("📊 Prediction Result")

        if result["prediction"] == 1:

            st.error("⚠️ HIGH RISK")

            st.warning(
                "This applicant is likely to default on the loan."
            )

        else:

            st.success("✅ LOW RISK")

            st.success(
                "This applicant is NOT likely to default on the loan."
            )

        st.metric(
            label="Prediction",
            value=result["prediction"]
        )

        with st.expander("📦 View API Response"):

            st.json(result)

    else:

        st.error("❌ Something went wrong while contacting the API.")

        st.code(response.text)

# -----------------------------
# FOOTER
# -----------------------------
st.divider()

st.caption(
    "Developed by **Funbi Opemipo Olowojesiku** | "
    "AnalystLab Africa Machine Learning Internship Capstone Project"
)