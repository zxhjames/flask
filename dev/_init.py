'''
Author: your name
Date: 2021-02-22 10:18:13
LastEditTime: 2021-02-22 10:33:08
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /PyCode/project_demo/flask/dev/__init__.py
'''

from flask import Flask, json,request,jsonify
# 初始化项目app
def create_app():
    app = Flask(__name__)
    return app