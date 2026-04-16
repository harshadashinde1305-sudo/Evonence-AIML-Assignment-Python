 Missing Value Handling
Python
import pandas as pd

def handle_missing_income(df):
    skewness = df["income"].skew()
    
    if abs(skewness) < 0.5:
        df["income"].fillna(df["income"].median(), inplace=True)
    else:
        df["income"].fillna(df["income"].mode()[0], inplace=True)
    
    return df
