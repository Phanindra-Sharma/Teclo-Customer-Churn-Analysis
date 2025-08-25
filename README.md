# 📊 Telco Customer Churn Analysis

## 📌 Project Overview
Customer churn is when a customer stops using a company’s service. Predicting churn helps businesses reduce revenue loss by targeting at-risk customers with retention strategies.  

In this project, I built an **end-to-end data analysis & machine learning pipeline** to predict customer churn for a telecom company.  

---

## 🗂️ Dataset
- **Source:** Telco Customer Churn Dataset  
- **Size:** 7043 rows × 30 columns  
- **Target Variable:** `Churn` (Yes/No)  
- **Features:** Customer demographics, subscribed services, contract details, billing & payment information  

---

## 🔍 Exploratory Data Analysis (EDA)
Key findings from EDA:
- **27% customers churned** → Imbalanced dataset  
- **Month-to-month contracts** have the highest churn  
- **Fiber optic internet users** churn more than DSL users  
- **High monthly charges** are strongly linked with churn  
- **Longer tenure customers** are less likely to churn  

*Example Plots:*  
- Churn % by Contract Type  
- Monthly Charges distribution by Churn  
- Churn rate by Internet Service  

---

## 🛠️ Data Preprocessing
- Handled missing values (`TotalCharges`, `MultipleLines`)  
- Encoded categorical variables (dummy variables & flags)  
- Engineered new features:  
  - `TotalServices` = number of services subscribed  
  - `HighMonthlyChargesFlag` = 1 if MonthlyCharges > 70  
  - `LongTenureFlag` = 1 if tenure > 50 months  
- Dropped irrelevant columns (`customerID`)  

---

## 🤖 Modeling
- **Model Used:** Logistic Regression (simple, interpretable baseline)  
- **Train/Test Split:** 80/20  
- **Scaling:** StandardScaler for numeric columns  

**Results:**  
- Accuracy: **0.82**  
- Precision (Churn): **0.68**  
- Recall (Churn): **0.60**  
- F1-score (Churn): **0.64**  

---

## 📈 Insights
- Customers with **month-to-month contracts** are most likely to churn  
- **High monthly charges** and **Fiber optic internet** increase churn risk  
- **Long-tenure customers** are less likely to churn  
- Senior citizens churn slightly more than non-senior citizens  

---

## 🏆 Recommendations
- Offer **discounted long-term contracts** to month-to-month customers  
- Investigate service quality issues for Fiber Optic users  
- Provide **loyalty rewards** to long-tenure customers  
- Apply targeted retention campaigns for high-charging customers  

---

## ⚙️ Tech Stack
- **Languages:** Python, SQL  
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn  
- **Environment:** Jupyter Notebook  

---

## 📂 Project Structure
