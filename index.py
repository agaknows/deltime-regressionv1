from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import requests
#api_url = "https://deltime-regressionv1.herokuapp.com/"
#response = requests.get(url, headers=header)

app = Flask(__name__)

delivery = pd.read_csv("deliverytime.csv")
deltime = delivery['deltime']
ncases = delivery['ncases']
distance = delivery['distance']


def lrfunction(vector1, vector2):
    
    delivery = pd.read_csv("deliverytime.csv")
    deltime = delivery['deltime']
    ncases = delivery['ncases']
    distance = delivery['distance']
    
    x=delivery[['ncases','distance']]
    y=delivery['deltime']
    
    regressor = LinearRegression()
    regressor.fit(x,y)
    
    b0 = regressor.intercept_
    b1 = regressor.coef_[0]
    b2 = regressor.coef_[1]
    
    userinput1=pd.Series(float(input("Please enter ncases: ")))
    userinput2=pd.Series(float(input("Please enter distance: ")))
    userinput3=pd.Series(float(input("Please enter delivery time: ")))
    
    finaldeltime = str( (b1*userinput1) + (b2*userinput2) + b0)
    return "deltime =" + finaldeltime


    

def lrfunction2(vector1, vector2):
    
    
    delivery = pd.read_csv("deliverytime.csv")
    deltime = delivery['deltime']
    ncases = delivery['ncases']
    distance = delivery['distance']
    
    userinput1=pd.Series(float(input("Please enter ncases: "))) #ncases input
    ncases = ncases.append(userinput1)
    ncases = pd.DataFrame(ncases)

    userinput2=pd.Series(float(input("Please enter distance: "))) #distance input
    distance = distance.append(userinput2)
    distance = pd.DataFrame(distance)
    
    userinput3=pd.Series(float(input("Please enter delivery time: "))) #deltime input
    deltime = deltime.append(userinput3)
    deltime = pd.DataFrame(deltime)
    
    delll = pd.concat([ncases, distance, deltime], axis = 1, ignore_index=True)
    delll.columns = ['ncases','distance','deltime']
    
    print(delll)
    
    x=delll[['ncases','distance']]
    y=delll['deltime']
    
    regressor = LinearRegression()
    regressor.fit(x,y)
    
    b0 = regressor.intercept_
    b1 = regressor.coef_[0]
    b2 = regressor.coef_[1]
    
    return "deltime = " + str(b1) + "(ncases) + " + str(b2) + "(distance) + " + str(b0)




@app.get("/regression")
def get_reg():
    headers = request.headers
    auth = headers.get("api-key")
    if auth == "mypassword":
        return jsonify (lrfunction(ncases, distance))
    else:
        return jsonify({"message":"Error: unauthorized"}),401
    
@app.post("/regression")
def get_reg2():
    headers = request.headers
    auth = headers.get("api-key")
    if auth == "mypassword":
        return jsonify (lrfunction2(ncases, distance))
    else:
        return jsonify({"message":"Error: unauthorized"}),401


if __name__ == '__main__':
    app.run()
    
#%%
api_url = "http://127.0.0.1:5000/regression"
headers={'Content-type': 'application/json', 'Accept': 'text/plain', 'api-key': 'mypassword'}

response=requests.get(api_url,headers=header)
print(response.json())

response=requests.post(api_url,headers=header)
print(response.json())
