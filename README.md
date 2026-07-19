# 💳 Loan Default Prediction System

## 📌 Project Overview

This project is an end-to-end Machine Learning application that predicts whether a customer is likely to default on a loan based on financial and personal information.

The project was developed as the Capstone Project for the AnalystLab Africa Machine Learning Internship.

---

## 🎯 Problem Statement

Financial institutions lose millions due to loan defaults. Accurately predicting loan default risk helps banks and lenders make better lending decisions, reduce financial losses, and improve customer risk management.

---

## 📊 Dataset

Source: Kaggle Loan Default Dataset

The dataset contains applicant information such as:

- Age
- Annual Income
- Loan Amount
- Credit Score
- Employment Status
- Marital Status
- Education
- Loan Purpose
- Interest Rate
- Loan Term
- Mortgage Status
- Co-signer Status
- Dependents

---

## 🛠 Data Preprocessing

The following preprocessing steps were performed:

- Missing value handling
- Duplicate removal
- Categorical variable encoding
- Feature selection
- Data preparation for Machine Learning

---

## 📈 Exploratory Data Analysis

EDA included:

- Summary Statistics
- Distribution plots
- Correlation Analysis
- Loan default trends
- Feature relationships

---

## 🤖 Machine Learning Model

Model Used:

- Random Forest Classifier

Reason:

Random Forest performs well on structured tabular data and handles nonlinear relationships effectively while reducing overfitting.

---

## 📊 Model Evaluation

Evaluation metrics included:

- Accuracy
- Precision
- Recall
- F1 Score

The trained model was saved using Joblib.

---

## 🚀 Deployment

Backend:
- FastAPI

Frontend:
- Streamlit

Deployment:
- Render

---

## 🧰 Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Streamlit
- Joblib
- Git
- GitHub
- Render

---

## 📁 Project Structure

loan-default-risk-analysis/

├── app.py

├── streamlit_app.py

├── requirements.txt

├── loan_default_model.joblib

├── label_encoders.joblib

├── README.md

└── LOAN_DEFAULT_APP.ipynb

---

## 📸 Application

The application allows users to enter applicant details and instantly predicts whether the loan is likely to default.

---

## 🎓 Internship

AnalystLab Africa Machine Learning Internship

Capstone Project

---

## 👤 Author

**Funbi Opemipo Olowojesiku**

GitHub:
https://github.com/Funbi-data

LinkedIn:
https://linkedin.com/in/funbiolowojesiku