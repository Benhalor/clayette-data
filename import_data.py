import pandas as pd
import os

def import_data():
    months = dict()
    entries = os.listdir('data/')
    for filename in entries:
        if 'csv' in filename:
            #print(filename)
            df =(pd.read_csv('data/'+filename))
            #df.columns = df.iloc[0]
            months[filename.replace('.csv','')] = df
            #print(df)
            #break
            
    return months
#print((months))
#print(months['mars22']['Type'])
