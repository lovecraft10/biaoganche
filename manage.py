#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import json
from flask import Flask, g, jsonify, make_response, request
from flask_cors import CORS
from flask_httpauth import HTTPBasicAuth
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData
from toolBackend.entiy.carCollection import Doors, Trip
from toolBackend.entiy.Admin import Admin, Fuel
import folium
from folium.plugins import HeatMap
import pymysql

from utils.mysqlUtils import getMoney, moneyRate, buyYear

app = Flask(__name__)
# r'/*' 是通配符，让本服务器所有的 URL 都允许跨域请求
CORS(app, resources=r'/*')
'''
mysql的连接配置
'''
# conf = {
#     "user": "root",
#     "password": "Cuikunna123!@#",
#     "host": "10.255.23.2",
#     "port": "31817",
#     "db": "car"
# }
# # 本地数据库
# conf1 = {
#     "user": "root",
#     "password": "123456",
#     "host": "localhost",
#     "port": "3306",
#     "db": "car"
# }
# connection = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db}'.format(**conf1)
# app.config['SECRET_KEY'] = 'hard to guess string'
# app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config['SQLALCHEMY_RECORD_QUERIES'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = connection
# db = SQLAlchemy(app)
auth = HTTPBasicAuth()
CSRF_ENABLED = True
app.debug = True


# "0~20w", "20~40w", "40~60w", "60~80w", "80~100w", ">100w"
# 116, 74, 19, 8, 4, 9

# 获取价格区间
@app.route('/api/getMoney', methods=['GET'])
def getmoney():
    data = getMoney()
    ele, ele1, total = 0, 0, 0
    list1 = data['nums'].tolist()
    rateData = [0]*len(list1)
    while (ele < len(list1)):
        total = total + list1[ele]
        ele += 1
    while (ele1 < len(list1)):
        rateData[ele1] = round(list1[ele1] / total, 4)
        ele1 += 1
    return jsonify({'code': 200, 'money': data['moneyRange'].tolist(), 'nums': data['nums'].tolist(), 'rate': rateData})

# 购买年限区间
@app.route('/api/getYear', methods=['GET'])
def getBuyYear():
    data = buyYear()
    ele, ele1, total = 0, 0, 0
    list1 = data['nums'].tolist()
    rateData = [0]*len(list1)
    while (ele < len(list1)):
        total = total + list1[ele]
        ele += 1
    while (ele1 < len(list1)):
        rateData[ele1] = round(list1[ele1] / total, 4)
        ele1 += 1
    return jsonify({'code': 200, 'year': data['yearRange'].tolist(), 'nums': data['nums'].tolist(), 'rate': rateData})

if __name__ == '__main__':
    app.run()
