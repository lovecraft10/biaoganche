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
import numpy as np
from clickhouse_sqlalchemy import make_session
from sqlalchemy import Table, Column, Integer, String, DateTime, BIGINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, MetaData, literal, ForeignKey
from entiy.Screen import StandingBook
from utils.mysqlUtils import getMoney, moneyRate, buyYear, standingBook, carCount, carName

import json
import datetime


# json方法重写
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')

        elif isinstance(obj, datetime.date):
            return obj.strftime("%Y-%m-%d")

        else:
            return json.JSONEncoder.default(self, obj)


app = Flask(__name__)
# r'/*' 是通配符，让本服务器所有的 URL 都允许跨域请求
CORS(app, resources=r'/*')

'''
mysql的连接配置
'''
conf1 = {
    "user": "root",
    "password": "123456",
    "host": "localhost",
    "port": "3306",
    "db": "car"
}
connection = 'mysql+pymysql://{user}:{password}@{host}:{port}/{db}'.format(**conf1)

engine = create_engine(connection)
session = make_session(engine)
metadata = MetaData(bind=engine)
Base = declarative_base(metadata=metadata)

# conf = {
#     "user": "root",
#     "password": "Cuikunna123!@#",
#     "host": "10.255.23.2",
#     "port": "31817",
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
    rateData = [0] * len(list1)
    while (ele < len(list1)):
        total = total + list1[ele]
        ele += 1
    while (ele1 < len(list1)):
        rateData[ele1] = round(list1[ele1] / total, 4)
        ele1 += 1
    return jsonify({'code': 200, 'money': data['moneyRange'].tolist(), 'nums': data['nums'].tolist(), 'rate': rateData})


# 购买年限占比
@app.route('/api/getYear', methods=['GET', 'POST'])
def getBuyYear():
    data = buyYear()
    dict1 = data.to_dict('records')
    # ele, ele1, total = 0, 0, 0
    # list1 = data['nums'].tolist()
    # rateData = [0] * len(list1)
    # while (ele < len(list1)):
    #     total = total + list1[ele]
    #     ele += 1
    # while (ele1 < len(list1)):
    #     rateData[ele1] = round(list1[ele1] / total, 4)
    #     ele1 += 1
    return jsonify({'code': 200, 'yearData': data['yearRange'].tolist(), 'info': dict1})


# 借用列表
@app.route('/api/getBook', methods=['GET'])
def getStandingBook():
    # 映射类查询方式
    query = session.query
    Infos = query(StandingBook)
    total = Infos.count()
    # dict1 = standingBook()
    return jsonify({'code': 200, 'total': total, 'info': [u.to_dict() for u in Infos]})
    # return jsonify({'code': 200, 'info': dict1})


# 获取表的一些总数的计算，标杆车数， 电车数量，左舵无牌等等等。。。。
@app.route('/api/getCount', methods=['GET', 'POST'])
def getCount():
    dict = carCount()
    return jsonify({'code': 200, 'info': dict})


# # 最近借出。。。。。
# @app.route('/api/recentStanding', methods=['GET'])
# def getRecent():
#     return 1


# 车辆品牌统计/占比
@app.route('/api/getBrand', methods=['GET'])
def getBrand():
    brandDict = carName()
    return jsonify({'code': 200, 'info': brandDict})

if __name__ == '__main__':
    app.run()
