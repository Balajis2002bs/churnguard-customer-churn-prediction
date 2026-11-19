import pandas as pd
import joblib


model=joblib.load(r'models/churn_prediction_model.joblib')
le=joblib.load(r'models/le_churn_prediction_model.joblib')


def predict(data):
    df=pd.DataFrame([data])
    predict=model.predict(df)
    predict=le.inverse_transform(predict)
    
    return predict[0]