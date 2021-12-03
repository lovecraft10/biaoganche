import json
import pandas as pd
import pymysql.cursors
import numpy as np
from flask import Flask, g, jsonify, make_response, request
from sqlalchemy.orm import sessionmaker
from toolBackend.common.transform import moneyRate, yearRange
# 引入多线程的信号量互斥查询
import threading

mutex = threading.Semaphore()
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='123456',
                       db='car',
                       cursorclass=pymysql.cursors.DictCursor)

# sql = '''
# select car_name from car_list
# '''

cursor = conn.cursor()


# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)
# 获取mysql表结构, 参数为表的名称
def getTable(tableName):
    sql = "desc {}".format(tableName)
    sql1 = '''
    select COLUMN_NAME from information_schema.COLUMNS where table_schema = 'car' and table_name = 'car_standing_book'
    '''
    mutex.acquire()
    cursor.execute(sql)
    mutex.release()
    result = cursor.fetchall()
    columns = []
    for i in range(len(result)):
        columns.append(result[i][0])
    # print(columns)
    return columns


# 获取价格相关数据
def getMoney():
    sql = '''
        select money from car_list where money is not null
    '''
    mutex.acquire()
    cursor.execute(sql)
    mutex.release()
    result = cursor.fetchall()
    df = pd.DataFrame(result)
    df.columns = ['money']
    df['money'] = df['money'].apply(lambda x: moneyRate(x))
    m1 = df['money'].tolist()
    m1_count = pd.Series(m1)
    countDict = dict(m1_count.value_counts(sort=False))
    df1 = pd.DataFrame(pd.Series(countDict), columns=['nums'])
    df1 = df1.reset_index().rename(columns={'index': 'moneyRange'})
    # print(countDict_key_ordered)
    return df1


# 购买年限
def buyYear():
    sql = '''
        select ((to_days(now()) - to_days(buy_date)) / 365) as buy_year 
        from car_list
        where buy_date is not null
    '''
    mutex.acquire()
    cursor.execute(sql)
    mutex.release()
    result = cursor.fetchall()
    df = pd.DataFrame(result)
    df.columns = ['year']
    df['year'] = df['year'].apply(lambda x: yearRange(x))
    m1 = df['year'].tolist()
    m1_count = pd.Series(m1)
    countDict = dict(m1_count.value_counts(sort=False))
    df1 = pd.DataFrame(pd.Series(countDict), columns=['nums'])
    df1 = df1.reset_index().rename(columns={'index': 'yearRange'})
    dict1 = df1.to_dict('records')

    return df1


# 借用表

def standingBook():
    sql = '''
        select * from standing_book
    '''
    mutex.acquire()
    cursor.execute(sql)
    mutex.release()
    result = cursor.fetchall()
    result1 = list(result)
    df = pd.DataFrame(result)
    df.columns = getTable("car_standing_book")
    dict = df.to_dict('records')
    print(df)
    print(dict)

    return dict


# 使用率
def UsageRateYear():
    sql = '''
        select usage_rate_year from car_list
    '''


# r2 = np.array(r1)
# print(r2[1])

# 统计表
def carCount():
    sql = '''
        select count(*) as total,
        count(license) as license,
        count(if(standard_rudder='左舵' and license is null, 1, null)) as left_no_license,
        count(if(standard_rudder='右舵', 1, null) ) as right_license,
        count(if(standard_rudder='中置', 1, null)) as middle,
        count(if(elding_mode='电动', 1, null)) as electric
        from car_list;
    '''
    mutex.acquire()
    cursor.execute(sql)
    mutex.release()
    result = cursor.fetchall()
    df = pd.DataFrame(result)
    # df.columns = ['total', 'license', 'left_no_license', 'right_license', 'middle', 'electric']
    df2 = pd.DataFrame(df.values.T, index=df.columns, columns=df.index)
    df2.columns = ['nums']
    df2['title'] = ['标杆车数量', '有牌车数量', '左舵无牌数量', '右舵样本车', '中置', '电动车']
    dict1 = df2.to_dict('records')

    return dict1

#车辆品牌
def carName():
    sql = '''
        select  substring_index(carName, CHAR(10), 1) as Name
        from (
         select substring_index(car_name, '|', 1) as carName
         from car_list
        ) as a;
    '''
    mutex.acquire()
    cursor.execute(sql)
    mutex.release()
    result = cursor.fetchall()
    df = pd.DataFrame(result)
    # df.columns = ['year']
    # df['year'] = df['year'].apply(lambda x: yearRange(x))
    m1 = df['Name'].tolist()
    m1_count = pd.Series(m1)
    countDict = dict(m1_count.value_counts())
    df1 = pd.DataFrame(pd.Series(countDict), columns=['nums'])
    df1 = df1.reset_index().rename(columns={'index': 'brand'})
    dict1 = df1.to_dict('records')
    # print(df)
    # print(df1)
    # print(dict1)
    return dict1