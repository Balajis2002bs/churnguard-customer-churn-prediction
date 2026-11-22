import pandas as pd
import joblib


model=joblib.load(r'models/churn_prediction_model.joblib')
le=joblib.load(r'models/le_churn_prediction_model.joblib')
baseline_model=joblib.load(r'models/baseline_model.joblib')

def predict(data):
    df=pd.DataFrame([data])
    predict=model.predict(df)
    baseline=baseline_model.predict(df)
    churn=le.inverse_transform(predict)
    baseline_churn=le.inverse_transform(baseline)
    prob=model.predict_proba(df)
    return churn[0],prob.max(),baseline_churn[0]