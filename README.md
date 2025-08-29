# 📊 Telco Customer Churn Prediction & Dashboard

A complete **end-to-end Data Analytics & Machine Learning project** on the popular **Telco Customer Churn dataset**.  
This project demonstrates data cleaning (SQL + Python), exploratory data analysis (EDA), feature engineering, **basic predictive modeling**, and interactive insights using **Power BI**.

---

## 📑 Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Project Workflow](#project-workflow)
  - [1. Data Cleaning (SQL & Python)](#1-data-cleaning-sql--python)
  - [2. Exploratory Data Analysis (EDA)](#2-exploratory-data-analysis-eda)
  - [3. Feature Engineering](#3-feature-engineering)
  - [4. Predictive Modeling (Basic)](#4-predictive-modeling-basic)
  - [5. Power BI Dashboard](#5-power-bi-dashboard)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

---

## 📌 Project Overview
Customer churn (the percentage of customers who stop using a company’s service) is a critical business problem.  
This project answers:
- Which customers are at high risk of churn?
- What key factors drive churn (e.g., tenure, monthly charges, contract type)?
- Can we predict churn using machine learning?
- How can we visualize churn insights interactively in **Power BI**?

---

## 📂 Dataset
The dataset used is the **Telco Customer Churn dataset**, which includes:
- **Customer Information**: Gender, SeniorCitizen, Partner, Dependents  
- **Services Signed Up**: Phone, Internet, OnlineSecurity, Streaming, etc.  
- **Billing & Contract Info**: Contract type, Payment method, Monthly & Total charges  
- **Target Variable**: `Churn` (Yes/No)

👉 [Download Dataset](https://www.kaggle.com/blastchar/telco-customer-churn)  

---

## 🔄 Project Workflow

### 1. Data Cleaning (SQL & Python)
- Imported raw dataset into **SQL** for structured cleaning.  
- Removed duplicates & invalid entries (e.g., blank `TotalCharges`).  
- Created flags (binary columns) in SQL: `PartnerFlag`, `PhoneServiceFlag`, `PaperlessBillingFlag`, etc.  
- Exported SQL-cleaned data → processed further in **Python** (handled nulls, type conversions).

### 2. Exploratory Data Analysis (EDA)
- Summary statistics, distributions & missing values check.  
- Visualized churn patterns by demographics, services, contract type.  
- Example EDA Insights:
  - Month-to-month customers churn the most.
  - Higher churn for customers with **higher monthly charges**.
  - Long-tenure customers are more loyal.

### 3. Feature Engineering
- Encoded categorical variables (One-Hot Encoding).  
- Created derived features:
  - `TotalServices` = count of services used.  
  - `HighChargesFlag` = 1 if monthly charges > median.  
- Handled missing values (imputation for `MultipleLines`).

### 4. Predictive Modeling (Basic)
- Model: **Logistic Regression** (beginner-friendly).  
- Accuracy: **~82%**  
- Confusion Matrix:
  - Precision (Churn=1): 0.68  
  - Recall (Churn=1): 0.60  
- Balanced performance for identifying churn customers.

### 5. Power BI Dashboard
An interactive **Churn Analysis Dashboard** was created with 5 key sections:

1. **Overall Customer Overview**  
   - Customer distribution by gender, contract, internet service.  
   - Churn rate KPI.

2. **Services & Churn Patterns**  
   - Service usage breakdown (Phone, Internet, Streaming).  
   - Churn comparison by service type.

3. **Financial Analysis**  
   - Monthly charges distribution split by churn.  
   - Average monthly charges card (with churn conditional color).  

4. **Customer Demographics**  
   - Churn split by gender, senior citizen, and dependents.  
   - Box plot of monthly charges vs churn.  

5. **Churn Risk & Insights**  
   - Tenure group vs churn (stacked column).  
   - Contract type impact on churn.  
   - High-risk customer segment identification.

---
## 🌟 Features

- SQL + Python dual cleaning approach.

- Beginner-friendly basic predictive modeling.

- Business-ready Power BI dashboard with actionable insights.

---
## 📜 License

This project is licensed under the MIT License – feel free to use and modify.
