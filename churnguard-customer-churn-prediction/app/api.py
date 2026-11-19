from fastapi import FastAPI
from app.schemas import Customer_Data
from app.services import predict as  predict_churn
app=FastAPI()



@app.post('/predict')
def predict(data: Customer_Data):
    prediction = predict_churn(data.model_dump())
    
    return {'prediction': prediction}