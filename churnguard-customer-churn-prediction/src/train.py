import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
from sklearn.metrics import classification_report,accuracy_score,precision_score,recall_score,confusion_matrix
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
from sklearn.model_selection import train_test_split
from datetime import datetime
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from pathlib import Path
class Train_Model:
    def __init__(self,df: pd.DataFrame):
        self.df=df
        Path('models').mkdir(exist_ok=True,parents=True)
        
    
    
    def evaluate_score(self,y_true,y_pred):
        print(round(accuracy_score(y_true,y_pred),3))
        print(round(precision_score(y_true,y_pred),3))
        print(round(recall_score(y_true,y_pred),3))
        con_mat=confusion_matrix(y_true,y_pred)
        print(con_mat)   
        

    def train(self):
        df=self.df
        print(df.head())
        le=LabelEncoder()

        y=le.fit_transform(df['Churn'])
        X=df[['gender', 'PhoneService', 'InternetService', 'Contract', 'PaperlessBilling', 'PaymentMethod']]

        preprocessing=ColumnTransformer(
            transformers=[
                ('one hot encoing',OneHotEncoder(drop='first',handle_unknown='ignore'),['gender', 'PhoneService', 'InternetService', 'Contract', 'PaperlessBilling', 'PaymentMethod'])

            ]
        )
        X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

        

        
        model_pipeline=Pipeline(
            steps=[
                ('preprocessing',preprocessing),
                ('model',LogisticRegression(max_iter=1000))
            ]
        )

        model_pipeline.fit(X_train,y_train)
        
        test_predictions=model_pipeline.predict(X_test)
        self.evaluate_score(y_test,test_predictions)


        model_name=datetime.now().strftime('%y-%m-%d_%H-%M-%S')
        joblib.dump(model_pipeline,f'models\\churn_prediction_model.joblib')
        joblib.dump(le,'models\\le_churn_prediction_model.joblib')
        # print(lr.feature_names_in_)
        
        return f'churn_prediction_model.joblib'
    
    
    
    
    
        

