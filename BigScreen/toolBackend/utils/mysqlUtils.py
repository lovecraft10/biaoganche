import pandas as pd
import pymysql.cursors
import numpy as np
conn = pymysql.connect(host='localhost',
                  user='root',
                             password='123456',
                             db='car')

# sql = '''
# select car_name from car_list
# '''

cursor = conn.cursor()
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)

# 定义价格区间
def moneyRate(x):
    if 0<=x< 200000:
        return ('0~20w')
    if 200000<=x<400000:
        return ('20~40w')
    if 400000<=x<600000:
        return ('40~60w')
    if 600000<=x<800000:
        return ('60~80w')
    if 800000<=x<1000000:
        return ('80~100w')
    if x>=1000000:
        return('>100w')

#购买年限区间的转换
def yearRange(x):
    if 0<=x< 2:
        return ('0~2年')
    if 2<=x<4:
        return ('2~4年')
    if 4<=x<6:
        return ('4~6w')
    if 6<=x<8:
        return ('6~8w')
    if 8<=x<10:
        return ('80~10w')
    if x>=10:
        return('>100w')
#获取价格相关数据
def getMoney():
    sql = '''
        select money from car_list
    '''
    cursor.execute(sql)
    result = cursor.fetchall()
    df = pd.DataFrame(result)
    df.columns = ['money']
    df['money'] = df['money'].apply(lambda x : moneyRate(x))
    m1 = df['money'].tolist()
    m1_count = pd.Series(m1)
    countDict = dict(m1_count.value_counts(sort=False))
    df1 = pd.DataFrame(pd.Series(countDict), columns=['nums'])
    df1 = df1.reset_index().rename(columns={'index': 'moneyRange'})
    # print(countDict_key_ordered)
    return df1

def buyYear():
    sql = '''
        select buy_year from car_list_brand 
    '''