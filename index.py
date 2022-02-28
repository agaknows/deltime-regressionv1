from flask import Flask, request, jsonify
import pandas as pd
import requests
#api_url = "https://deltime-regressionv1.herokuapp.com/"
#response = requests.get(url, headers=header)

app = Flask(__name__)


delivery = pd.read_csv("deliverytime.csv")

deltime = delivery['deltime']
ncases = delivery['ncases']
distance = delivery['distance']


def corrfunction(vector1, vector2):
    
    v1mean = vector1.mean()
    v1std = vector1.std()
    v1=[]
    
    for i in vector1:
        v1.append((i-v1mean)/v1std)
        
    v2mean = vector2.mean()
    v2std = vector2.std()
    v2 = []
    
    for i in vector2:
        v2.append((i-v2mean)/v2std)
        
    
    df =pd.DataFrame([v1,v2])
    df_t=df.T
    
    
    df_t['Product']= (df_t[0]*df_t[1])
    
    reg = (df_t['Product'].sum())/(len(df_t)-1)
    return(reg)


@app.get("/regression")
def get_reg():
    return jsonify (corrfunction(ncases, distance))
    

if __name__ == '__main__':
    app.run()
    
#%%
api_url = "http://127.0.0.1:5000/regression"
response=requests.get(api_url)
print(response.json())
