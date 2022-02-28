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

type(deltime)

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

def corrfunction2(vector1, vector2):
    
    v1mean = vector1.mean()
    v1std = vector1.std()
    v1=[]
    
    userinput1=pd.Series(float(input("Please enter ncases: "))) #ncases input
    vector1 = vector1.append(userinput1)
    for i in vector1:
        v1.append((i-v1mean)/v1std)
    
        
    v2mean = vector2.mean()
    v2std = vector2.std()
    v2 = []
    
    userinput2=pd.Series(float(input("Please enter distance: "))) #distance input
    vector2 = vector2.append(userinput2)
    for i in vector2:
        v2.append((i-v2mean)/v2std)
    
    userinput3=pd.Series(float(input("Please enter delivery time: "))) #deltime input
    
    df =pd.DataFrame([v1,v2])
    df_t=df.T
    
    print(df_t)
    
    df_t['Product']= (df_t[0]*df_t[1])
    
    reg = (df_t['Product'].sum())/(len(df_t)-1)
    return(reg)

@app.get("/regression")
def get_reg():
    headers = request.headers
    auth = headers.get("api-key")
    if auth == "mypassword":
        return jsonify (corrfunction(ncases, distance))
    else:
        return jsonify({"message":"Error: unauthorized"}),401
    
@app.post("/regression")
def get_reg2():
    headers = request.headers
    auth = headers.get("api-key")
    if auth == "mypassword":
        return jsonify (corrfunction2(ncases, distance))
    else:
        return jsonify({"message":"Error: unauthorized"}),401


if __name__ == '__main__':
    app.run()
    
#%%
api_url = "http://127.0.0.1:5000/regression"
headers={'Content-type': 'application/json', 'Accept': 'text/plain', 'api-key': 'mypassword'}

response=requests.get(api_url,headers=header)
print(response.json())
