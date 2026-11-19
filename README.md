# 🚀 ChurnGuard: Predicting Customer Exit Before It Happens

## 📖 Overview

ChurnGuard is an end-to-end Machine Learning application that predicts whether a telecom customer is likely to churn based on customer demographics and service usage information.

The project demonstrates the complete ML workflow from data cleaning to model deployment using FastAPI, Streamlit, and Docker.

---

## 🎯 Problem Statement

Customer churn is a critical challenge for telecom companies. Losing customers directly impacts revenue and growth.

The goal of this project is to build a machine learning solution capable of identifying customers at risk of churn so that organizations can take proactive retention measures.

---

## ✨ Features

- Data Cleaning and Preprocessing
- Exploratory Data Analysis (EDA)
- Logistic Regression Model Training
- Scikit-Learn Pipeline
- Model Persistence using Joblib
- FastAPI REST API
- Streamlit User Interface
- Docker Containerization
- End-to-End Prediction Pipeline

---

## 🛠️ Tech Stack

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-Learn

### Backend
- FastAPI
- Uvicorn

### Frontend
- Streamlit

### Deployment
- Docker
- Docker Compose

### Model Persistence
- Joblib

---

## 📊 Dataset

The project uses the Telco Customer Churn Dataset.

### Input Features

| Feature | Description |
|----------|------------|
| Gender | Customer Gender |
| PhoneService | Phone Service Availability |
| InternetService | Internet Service Type |
| Contract | Customer Contract Type |
| PaperlessBilling | Paperless Billing Status |
| PaymentMethod | Customer Payment Method |

### Target Feature

| Target | Description |
|----------|------------|
| Churn | Indicates whether the customer left the service |

---

## 🏗️ Project Architecture

```text
User
  ↓
Streamlit Frontend
  ↓
FastAPI Backend
  ↓
Machine Learning Pipeline
  ↓
Logistic Regression Model
  ↓
Prediction Response
```

---

## 📁 Project Structure

```text
ChurnGuard/
│
├── app/
│   ├── api.py
│   ├── schemas.py
│   └── services.py
│
├── frontend/
│   └── app.py
│
├── src/
│   ├── data_cleaning.py
│   ├── data_overview.py
│   ├── train.py
│   └── main.py
│
├── models/
│   ├── churn_prediction_model.joblib
│   └── le_churn_prediction_model.joblib
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── screenshots/
│
├── Dockerfile.fastapi
├── Dockerfile.streamlit
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Machine Learning Pipeline

### Preprocessing

Categorical features are encoded using:

```python
OneHotEncoder(handle_unknown="ignore", drop="first")
```

### Model

```python
LogisticRegression(max_iter=1000)
```

### Pipeline

```python
Pipeline([
    ("preprocessing", preprocessing),
    ("model", LogisticRegression(max_iter=1000))
])
```

---

## 🔌 API Endpoint

### Predict Customer Churn

**POST**

```http
/predict
```

### Request

```json
{
  "gender": "Male",
  "PhoneService": "Yes",
  "InternetService": "DSL",
  "Contract": "One year",
  "PaperlessBilling": "No",
  "PaymentMethod": "Bank Transfer"
}
```

### Response

```json
{
  "prediction": "No"
}
```

---

## 💻 Run Locally

### Clone Repository

```bash
git clone <your-github-repository-url>
cd ChurnGuard
```

### Install Dependencies


```bash
pip install -r requirements.txt
```

### Train Model

#### Run the training pipeline to generate processed datasets and trained models:

```bash
python src/main.py
```

### Start FastAPI

```bash
uvicorn app.api:app --reload
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

### Start Streamlit

```bash
streamlit run frontend/app.py
```

Streamlit UI:

```text
http://localhost:8501
```

---

## 🐳 Docker Deployment

Build and start all services:

```bash
docker compose up --build
```

### Services

| Service | URL |
|----------|------|
| FastAPI | http://localhost:8000/docs |
| Streamlit | http://localhost:8501 |

---

## 📸 Screenshots



### Prediction Result

![](screenshots/streamlit_app.png)

---

### FastAPI Swagger UI

![](screenshots/swagger_ui.png)

---

### Docker Containers Running

![](screenshots/docker_containers.png)

---


### Model Performance
![](screenshots/model_performance.png)

## 🔮 Future Improvements

- AWS EC2 Deployment
- CI/CD using GitHub Actions
- Random Forest Model
- XGBoost Model
- Hyperparameter Tuning
- Model Monitoring
- User Authentication

---

## 📚 Key Learning Outcomes

This project helped me gain hands-on experience in:

- Data Cleaning
- Feature Engineering
- Machine Learning Pipelines
- Classification Models
- Model Serialization
- REST API Development
- Streamlit Development
- Docker Containerization
- End-to-End ML Application Development

---

## 👨‍💻 Author

**Balaji S**

Aspiring AI/ML Engineer | Python Developer | FastAPI | Streamlit | Scikit-Learn | Docker

---

