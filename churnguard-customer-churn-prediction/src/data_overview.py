import pandas as pd


class Data_Overview:
    # def __init__(self,df: pd.DataFrame):
    #     self.df=df
    
    
    
    
    def overview(self,df):
        #First 5 rows
        print(df.head())
        #No. of rows and columns in dataset
        shape=df.shape
        print(f"The dataset has {shape[0]} rows and {shape[1]} columns.")
        #Basic info about the Dataset
        print(df.info())
        #Statistics about the Numerical Columns in Dataset
        print(df.describe())
        #Number of Null values in Dataset
        print(df.isna().sum())
        #Number of Duplicates in Dataset
        print(df.duplicated().sum())
        #Checking the inconsistency of Churn values
        print(df['Churn'].value_counts())
        #Checking typos in Contract columns
        print(df['Contract'].unique())
        
        

