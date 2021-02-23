'''
Author: your name
Date: 2021-02-22 10:20:16
LastEditTime: 2021-02-22 16:35:13
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /PyCode/project_demo/flask/dev/routes/routers.py
'''
from flask import Flask, json,request,jsonify
from . import weight_lineregression 
# 初始化项目app
app = Flask(__name__)


@app.route('/predict/lineregression',methods=['POST'])
def lineregression():
    d = request.get_json()
    x = d['x']
    y = d['y']
    n = d['n']
    t = d['t']
    # if valid_req_data(x,y,n) is False :
    #     return jsonify({
    #         "code": -1,
    #         "msg": "参数不符合要求"
    #     })
    
    res = Get_Predict_Ans(x,y,n,t)
    return jsonify({
        "code":200,
        "data":res
    })

# 参数校验
def valid_req_data(x,y,n):
    if len(x) != len(y) or n < 1:
        return False
    return True


def Get_Predict_Ans(x,y,n,t):
    res = ""
    if t == "线性回归":
        res = weight_lineregression.predict_lineregression(x,y,n)
        print("线性")

    if t == "加权线性回归":
        print("加权")

    if t == "prophet":
        res = weight_lineregression.predict_prophet(x,y,n)
        print("prophet")

    return jsonify({
        "res":res
    })

