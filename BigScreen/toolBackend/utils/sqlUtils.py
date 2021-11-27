import os
import sqlite3

import pandas as pd

basedir = os.path.abspath(os.path.dirname(__file__))
# url = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
conn = sqlite3.connect('/data.sqlite')
c = conn.cursor()


def timeTOfuel():
    sql1 = '''
        select reportTime, IP_AvgFuelCons from B01
        limit 100
    '''
    data = c.execute(sql1)
    all_logs = data.fetchall()
    df = pd.DataFrame(all_logs)
    # #获取数据表的结构信息
    # sql2 = '''
    #     pragma table_info(B01)
    # '''
    # col = c.execute(sql2)
    # col_result = col.fetchall()
    # columns1 = [0] * len(col_result)
    # for i in range(len(col_result)):
    #     columns1[i] = col_result[i][1]
    # df.columns = columns1

    df.columns = ['reportTime', 'IP_AvgFuelCons']
    # timeData = df['reportTIme']
    # fuelData = df['IP_AvgFuelCons']
    # print(df)
    # for log in all_logs:
    #     print(log)
    df['reportTime'] = pd.to_datetime(df['reportTime'])

    return df

timeTOfuel()