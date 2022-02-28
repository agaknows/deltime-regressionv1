import pandas as pd
import numpy as np
delivery = pd.read_csv("deliverytime.csv")

deltime = delivery['deltime']
ncases = delivery['ncases']
distance = delivery['distance']


def corrfunction(ncases, distance):
    
    v1mean = ncases.mean()
    v1std = ncases.std()
    v1=[]
    
    for i in ncases:
        v1.append((i-v1mean)/v1std)
        
    v2mean = distance.mean()
    v2std = distance.std()
    v2 = []
    
    for i in distance:
        v2.append((i-v2mean)/v2std)
        
    
    df =pd.DataFrame([v1,v2])
    df_t=df.T
    
    print
    
    df_t['Product']= (df_t[0]*df_t[1])
    
    print((df_t['Product'].sum())/(len(df_t)-1))
    
