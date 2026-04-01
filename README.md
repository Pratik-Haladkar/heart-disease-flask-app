# ❤️ Heart Disease Prediction (Flask Version)

A production-style **Machine Learning web application** built using Flask that predicts the risk of heart disease based on medical parameters.

---

## 🚀 Features

* 🔍 Predicts heart disease risk using ML model
* 📊 Displays probability-based risk analysis
* 🌐 Clean and user-friendly web interface
* ⚙️ REST API support (`/predict_api`)
* 🧠 Built with Scikit-learn

---

## 🧠 Tech Stack

* Python
* Flask
* Scikit-learn
* NumPy
* HTML/CSS

---

## 📊 Input Features

* Age
* Sex
* Chest Pain Type
* Resting Blood Pressure
* Cholesterol
* Fasting Blood Sugar
* Rest ECG
* Max Heart Rate Achieved
* Exercise Induced Angina
* Oldpeak
* Slope
* Number of Major Vessels (ca)
* Thal

---

## 🧪 Test Cases (Dataset Samples)

### ✅ Test Case 1

```
46,1,0,140,311,0,1,120,1,1.8,1,2,3,0
```

**UI Input Mapping:**

* Age → 46
* Sex → Male
* Chest Pain → Typical Angina
* Resting BP → 140
* Cholesterol → 311
* Fasting Blood Sugar → Less than 120
* Rest ECG → ST-T Abnormality
* Max Heart Rate → 120
* Exercise Angina → Yes
* Oldpeak → 1.8
* Slope → Flat
* Major Vessels → 2
* Thal → Reversible Defect

👉 **Expected Output:** Low Risk ✅

---

### 🚨 Test Case 2

```
38,1,2,138,175,0,1,173,0,0,2,3,2,1
```

**UI Input Mapping:**

* Age → 38
* Sex → Male
* Chest Pain → Non-anginal
* Resting BP → 138
* Cholesterol → 175
* Fasting Blood Sugar → Less than 120
* Rest ECG → ST-T Abnormality
* Max Heart Rate → 173
* Exercise Angina → No
* Oldpeak → 0
* Slope → Downsloping
* Major Vessels → 3
* Thal → Fixed Defect

👉 **Expected Output:** High Risk 🚨

---

## ⚙️ How to Run Locally

```bash
git clone https://github.com/your-username/heart-disease-flask-app.git
cd heart-disease-flask-app
pip install -r requirements.txt
python app.py
```

Then open:

```
http://127.0.0.1:5000/
```

---

## 🌐 Deployment

This project can be deployed using platforms like Render or Railway.

---

## 🔥 Project Note

This is the **Flask-based version** of the project, focusing on:

* Backend development
* REST API implementation
* Structured web deployment

Unlike the Streamlit version, this simulates a **production-ready system**.

---

## 👨‍💻 Author

Pratik Haladkar
