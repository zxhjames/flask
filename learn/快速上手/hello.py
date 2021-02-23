'''
Author: your name
Date: 2021-02-21 10:25:31
LastEditTime: 2021-02-22 11:20:00
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /PyCode/project_demo/flask/learn/快速上手/1.py
'''

from flask import Flask, json
from flask import request
from flask import jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "hello world"

# 变量规则
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % escape(username)

@app.route('/post/<int:pos_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % escape(subpath)    

# url构建
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return "post"
    else:
        return "get"

# 使用表单处理请求
@app.route('/newlogin',methods=['POST','GET'])
def login_new():
    error = None
    if request.method == 'POST':
        if request.form['username'] == 'admin' and request.form['password'] == '123':
            return "ok"
        else:
            return "error"
    return error

# 使用json请求
@app.route("/me")
def me_api():
    return {
        "username" : "james",
        "password" : "123"
    }

class User:
    username = "admin"
    password = "123"

def __init__(self,name,pwd):
    self.name = 'aaa'
    self.pwd = pwd

@app.route("/json",methods=['GET'])
def get_user():
    u = User("james","123")
    return json(u)


@app.route('/predict/lineregression',methods=['POST'])
def lineregression():
    d = request.get_json()
    x = d['x']
    y = d['y']
    n = d['n']
    t = d['t']
    if valid_req_data(x,y,n) is False :
        return jsonify({
            "code": -1,
            "msg": "参数不符合要求"
        })
    
    res = Get_Predict_Ans(x,y,n,t)
    return jsonify({
        "code":200,
        "data":res
    })


def valid_req_data(x,y,n):
    if len(x) != len(y) or n < 1:
        return False
    return True

