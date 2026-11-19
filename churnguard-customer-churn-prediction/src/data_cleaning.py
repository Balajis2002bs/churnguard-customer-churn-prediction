import pandas as pd
from datetime import datetime
from pathlib import Path

class Data_Cleaning:
    
    Path('data\processed').mkdir(exist_ok=True,parents=True)
        
    
    def __init__(self,df):
        self.df=df
        
    
    def data_clean(self):
        
        df=self.df
        #Droping CustomerID column
        df=df.drop(columns=['customerID'])
        print(df.columns)
        #Dropping duplicates rows in the dataset
        df=df.drop_duplicates()
        df.duplicated().sum()
        #Stripping the whitespaces in categorical columns
        cat_cols=df.select_dtypes('object').columns
        for col in cat_cols:
            df[col]=df[col].str.strip().str.title()

        #Mapping the Contract values into three categories such as Month-to-month, One year, Two year
        df['Contract']=df['Contract'].str.lower()
        df['Contract']=df['Contract'].map({
        
            'month to month': 'Month-to-month',
            'month-to-month': 'Month-to-month',
            'monthly':'Month-to-month',
            '1 year': 'One year',
            'one year': 'One year',
            '2 year': 'Two year',
            'two year': 'Two year',
            
            
        })


        print(f"After Cleaning, Value counts for 'Contract': {df['Contract'].value_counts().to_dict()}")

        #Mapping Internet Service value into three categories such as Fiber optic, DSL, No
        print('Before Mapping InternetService: ')
        print(df['InternetService'].value_counts())
        print()
        df['InternetService']=df['InternetService'].str.strip().str.lower()
        df['InternetService']=df['InternetService'].map(
            {
            'dsl': 'DSL',
            'fiber optic': "Fiber optic",
            'fiberoptic':'Fiber optic',
            'fibre optic':'Fiber optic',
            'NaN' : 'No',
            'no' : 'No',
            
            }
        )
        df['InternetService']=df['InternetService'].fillna('No')
        print()

        print('After Mapping InternetService: ')
        print(df['InternetService'].value_counts())




        #Converting Total Charger into numeric columns 
        df['TotalCharges']=pd.to_numeric(df['TotalCharges'],errors='coerce')
        print(df['TotalCharges'].dtype)
        print()
        print(df['TotalCharges'].isna().sum())


        #Dropping rows where the tenure is zero or negative
        df=df.drop(df[df['tenure'] <=0].index )

        #Dropping rows where Total Charges below 10 and greater than 200
        df=df.drop(df[(df['TotalCharges'] <= 10 ) | (df['TotalCharges'] >= 200)].index )


        #Filling mean value for Monthly Charges and Total Charges
        for col  in ['MonthlyCharges','TotalCharges']:
            df[col]=df[col].fillna(df[col].mean())

        #Filling median value for Tenure

        df['tenure']=df['tenure'].fillna(df['tenure'].median().__round__(2))



        print('After Cleaning: ')
        print()
        print(f'In Cleaned Dataset, Total Rows: {df.shape[0]}, Total Columns: {df.shape[1]}')
        print()


        print(f'In Cleaned Dataset, Total Missing Values: {df.isna().sum()}')
        file_name=datetime.now().strftime('%y-%m-%d_%H%M%S')
        df.to_csv(f'data\\processed\\{file_name}_cleaned_data.csv',index=False)
        
        return f'{file_name}_cleaned_data.csv'
        
        
        


