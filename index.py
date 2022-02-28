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






@app.get("/regression")
def get_reg():
    headers = request.headers
    auth = headers.get("api-key")
    if auth == "mypassword":
    
        delivery = pd.read_csv("deliverytime.csv")
        deltime = delivery['deltime']
        ncases = delivery['ncases']
        distance = delivery['distance']
        
        input_ncases = int(headers.get("ncases"))
        input_distance = int(headers.get("distance"))
        
        x=delivery[['ncases','distance']]
        y=delivery['deltime']
        
        regressor = LinearRegression()
        regressor.fit(x,y)
        
        b0 = regressor.intercept_
        b1 = regressor.coef_[0]
        b2 = regressor.coef_[1]
        
        
        prediction = (b1*input_ncases) + (b2*input_distance) + b0
        regression = [{"ncases":input_ncases,"distance":input_distance, "response":"deltime","Prediction": prediction}]
        ans = pd.DataFrame(regression)
        ans = ans.to_json()
        return jsonify(ans), 200
    
    else:
        return jsonify({"message":"Error: unauthorized"}),401
    
@app.post("/regression")
def get_reg2():
    headers = request.headers
    auth = headers.get("api-key")
    if auth == "mypassword":
        
        delivery = pd.read_csv("deliverytime.csv")
        deltime = delivery['deltime']
        ncases = delivery['ncases']
        distance = delivery['distance']
        
        input_ncases = pd.Series(int(headers.get("ncases")))
        input_distance = pd.Series(int(headers.get("distance")))
        input_deltime = pd.Series(int(headers.get("deltime")))
        
        ncases = ncases.append(input_ncases)
        deltime = deltime.append(input_deltime)
        distance = distance.append(input_distance)
        
        x=delivery[['ncases','distance']]
        y=delivery['deltime']
        
        regressor = LinearRegression()
        regressor.fit(x,y)
        
        b0 = regressor.intercept_
        b1 = regressor.coef_[0]
        b2 = regressor.coef_[1]
        
        
        prediction = (b1*input_ncases) + (b2*input_distance) + b0
        regression = [{"ncases":input_ncases,"distance":input_distance, "response":"deltime","Prediction": prediction}]
        ans = pd.DataFrame(regression)
        ans = ans.to_json()
        return jsonify(ans), 200
        
        
    else:
        return jsonify({"message":"Error: unauthorized"}),401


if __name__ == '__main__':
    app.run()