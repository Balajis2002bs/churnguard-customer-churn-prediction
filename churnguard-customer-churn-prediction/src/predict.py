import joblib
import pandas as pd
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder


class Predict_Data:
    def __init__(self,df:pd.DataFrame,model_path:str):
        
        self.model_path=model_path
        self.df=df
    
    
    def predict(self):
        df=self.df
        model_path=self.model_path
        model=joblib.load(f'models\\{model_path}')
        le=joblib.load(f'models\\le_{model_path}')
        # le=LabelEncoder()
        
        y=df['Churn']
        X=df[['gender', 'PhoneService', 'InternetService', 'Contract', 'PaperlessBilling', 'PaymentMethod']]
        y_pred=model.predict(X)
        y_pred=le.inverse_transform(y_pred)
        
        print(classification_report(y,y_pred))
        



