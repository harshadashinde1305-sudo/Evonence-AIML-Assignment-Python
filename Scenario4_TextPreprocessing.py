Text Pre-processing
Python
import re

def preprocess_text(df, column):
    df[column] = df[column].str.lower()
    df[column] = df[column].apply(lambda x: re.sub(r'[^a-zA-Z0-9\s]', '', x))
    df[column] = df[column].apply(lambda x: x.split())
    return df
