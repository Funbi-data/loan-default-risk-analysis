#  Credit Risk Assessment & Loan Default Prediction

##  Project Overview
This project develops a machine learning-based credit risk model to predict loan default and support smarter financial decision-making.

The model identifies high-risk borrowers using financial and credit-related features, enabling lenders to reduce potential losses and improve risk management strategies.

##  Business Problem
Loan defaults pose a major financial risk to lending institutions. Traditional evaluation methods often fail to accurately identify high-risk customers, especially when dealing with imbalanced datasets.

This project aims to:
- Predict the likelihood of loan default
- Improve detection of high-risk borrowers
- Support data-driven lending decisions

##  Dataset Description
The dataset includes borrower-level financial and credit information such as:
- Credit Policy
- Interest Rate
- FICO Score
- Loan Purpose
- Income and other financial indicators

##  Data Preparation
- Cleaned and prepared dataset for analysis
- Converted categorical variables using One-Hot Encoding
- Split data into training and testing sets
- Addressed class imbalance using **SMOTE (Synthetic Minority Oversampling Technique)**

##  Modeling Approach
A **Random Forest Classifier** was used to build the predictive model.
Model improvements included:
- Increasing number of estimators
- Controlling tree depth to prevent overfitting
- Applying SMOTE to improve minority class detection

##  Model Performance
### Before Handling Imbalance:
- High overall accuracy
- Very low recall for defaulters (~2–3%)
- Model biased toward non-defaulters

### After Applying SMOTE:
- Recall improved significantly (~36%)
- Better detection of high-risk borrowers
- Slight reduction in accuracy (expected trade-off)

##  Key Insights
- **Credit Policy**, **Interest Rate**, and **FICO Score** are the strongest predictors of loan default
- Imbalanced data can lead to misleading performance metrics
- Recall is more critical than accuracy in risk prediction problems

##  Business Impact
- Enables financial institutions to identify risky borrowers earlier
- Helps reduce loan default losses
- Improves credit decision-making through data-driven insights


##  Key Features
- Loan default prediction using Machine Learning
- Improved recall using SMOTE
- Feature importance analysis
- Batch risk scoring system for multiple applicants
- Business decision recommendations (Approve, Review, Reject)


##  Tools & Technologies
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib


##  Conclusion
This project demonstrates how handling class imbalance significantly improves model effectiveness in financial risk prediction. By focusing on recall and applying SMOTE, the model becomes more practical for real-world lending decisions.


##  Author
**Funbi Opemipo Olowojesiku**  
Data Analyst | Machine Learning Enthusiast  
Open to Remote Opportunities
