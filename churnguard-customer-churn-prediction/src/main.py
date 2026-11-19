import data_overview,data_cleaning,train,predict
import pandas as pd
from fastapi import FastAPI

app=FastAPI()


df=pd.read_csv('data/raw/Telco-Customer-Churn.csv')

do=data_overview.Data_Overview()
dc=data_cleaning.Data_Cleaning(df)

do.overview(df)
print('data cleaning')
print()
print()
cleaned_file_name=dc.data_clean()
tm=train.Train_Model(pd.read_csv(f'data\\processed\\{cleaned_file_name}'))


# tp.predict()
model_path=tm.train()


#predict dataset

# pred_df=pd.read_csv('data\\raw\\churnguard_data.csv')
# pred_dc=data_cleaning.Data_Cleaning(pred_df)
# clean_pred_data= pred_dc.data_clean()



# tp=predict.Predict_Data(pd.read_csv(f'data\\processed\\{clean_pred_data}'),model_path)

# tp.predict()