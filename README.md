# Loan Default Risk Prediction API

## Overview

This project is a Machine Learning API that predicts whether a loan applicant is likely to default on a loan based on financial and demographic information.

The API was built with FastAPI and deployed on Render.

---

## Features

- Predict loan default risk
- REST API with FastAPI
- Interactive Swagger documentation
- Scikit-learn Machine Learning model
- Cloud deployment with Render

---

## Tech Stack

- Python
- FastAPI
- Scikit-learn
- Pandas
- Joblib
- Uvicorn
- Render
- Git & GitHub

---

## Project Structure

```
app.py
loan_default_model.joblib
label_encoders.joblib
requirements.txt
README.md
```

---

## API Endpoint

POST `/predict`

Example Response

```json
{
    "prediction": 0,
    "result": "Loan not likely to default"
}
```

---

## Live Demo

### API

https://loan-default-risk-analysis.onrender.com

### Swagger Docs

https://loan-default-risk-analysis.onrender.com/docs

---

## Author

Funbi Opemipo Olowojesiku

GitHub:
https://github.com/Funbi-data

LinkedIn:
https://linkedin.com/in/funbiolowojesiku