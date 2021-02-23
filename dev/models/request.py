'''
Author: your name
Date: 2021-02-22 10:25:07
LastEditTime: 2021-02-22 10:28:21
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /PyCode/project_demo/flask/dev/models/request.py
'''
# 请求参数

'''
请求参数的通用请求体,x时间,y历史预测值,n预测的天数
'''
class seriesdata:
    x = []
    y = []
    n = 0


def __init__(self,x,y,n):
    self.x = x
    self.y = y 
    self.n = n 

