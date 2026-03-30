# Exploratory Data Analysis (EDA) on Diabetes Dataset

## 📌 Project Overview

This project performs **Exploratory Data Analysis (EDA)** on the diabetes dataset to understand patterns, relationships, and key factors influencing diabetes prediction.

The dataset contains medical predictor variables and one target variable indicating whether a patient has diabetes.

Dataset source: diabetes.csv

## 📊 Dataset Description

The dataset includes the following features:

* Pregnancies
* Glucose
* BloodPressure
* SkinThickness
* Insulin
* BMI
* DiabetesPedigreeFunction
* Age
* Outcome (Target Variable)

These features represent clinical measurements used to assess diabetes risk ([GitHub][1]).



## 🎯 Objectives of EDA

* Understand dataset structure and data types
* Detect missing or zero values
* Identify correlations between variables
* Analyze distribution of features
* Study relationship between features and outcome

---

## 🧹 Data Cleaning

* Checked for missing values
* Replaced invalid zero values in:

  * Glucose
  * BloodPressure
  * BMI
  * Insulin
* Handled outliers where necessary

---

## 📈 Exploratory Analysis Performed

### 1. Univariate Analysis

* Distribution plots (histograms)
* Boxplots for outlier detection
* Observed skewness in features like Insulin and BMI

---

### 2. Bivariate Analysis

* Correlation heatmap
* Pairplots to visualize feature relationships

Key observations:

* Glucose shows strong correlation with Outcome
* BMI moderately affects diabetes risk
* Age and Pregnancies show some relationship

---

### 3. Multivariate Analysis

* Combined feature interactions
* Identified patterns contributing to higher diabetes probability

---

## 🔍 Key Insights

* Higher glucose levels strongly indicate diabetes
* BMI and age are significant contributing factors
* Some features contain unrealistic zero values → need preprocessing
* Dataset is slightly imbalanced

---

## 🛠️ Tools & Libraries Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn

---

## 📁 Project Structure

```
├── diabetes.csv
├── eda.ipynb
└── README.md
```

---

## 🚀 How to Run

1. Clone the repository
2. Install dependencies:

   ```
   pip install pandas numpy matplotlib seaborn
   ```
3. Run the notebook:

   ```
   jupyter notebook eda.ipynb
   ```

---

## 📌 Conclusion

EDA helped uncover key relationships and data issues that are critical before building machine learning models. Proper preprocessing significantly improves model performance.

---

## 🔗 Future Work

* Feature engineering
* Model building (Logistic Regression, Random Forest)
* Hyperparameter tuning
* Deployment

---

[1]: https://github.com/AdityaGupta1509/Diabetes-Predictor?utm_source=chatgpt.com "Diabetes Prediction Project"
