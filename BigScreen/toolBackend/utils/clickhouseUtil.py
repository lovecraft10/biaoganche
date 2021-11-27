# import pandas as pd
# from clickhouse_driver import Client
# import os
# import csv
# import datetime
# import warnings
# import matplotlib.pyplot as plt
# import time
#
# '''
# 使用clickhouse_driver连接clickhouse的工具类
# '''
# host = '10.255.128.201'
# port = 8000
# password = 'Abc123456!'
# # database='Database Native'
# send_receive_timeout = 5000  # 超时时间
# socket_timeout = 600000
# client = Client(host=host, port=port, password=password, send_receive_timeout=send_receive_timeout)
# sql = 'use default'
# client.execute(sql)
#
# '''
# 车门开关次数统计
# '''
#
#
# def doors():
#     sql = '''
#     select vin,
#             countIf(runningDifferenceStartingWithFirstValue(driver_door_sts)  as driverDoor,
#                driver_door_sts_valid = 1 and driverDoor = 1) as driverD,
#             countIf(runningDifferenceStartingWithFirstValue(passenger_door_sts) as passengerDoor,
#                 passenger_door_sts_valid = 1 and passengerDoor = 1) as passengerD,
#             countIf(runningDifferenceStartingWithFirstValue(rr_door_sts) as rrDoor,
#                 rr_door_sts_valid = 1 and rrDoor = 1) as rrD,
#             countIf(runningDifferenceStartingWithFirstValue(rl_door_sts) as rlDoor,
#                 rl_door_sts_valid = 1 and rlDoor = 1) as rlD
#     from
#     chb121_glgd_loc
#     group by vin
#     limit 10000
#     '''
#     data = client.execute(sql)
#     data1 = pd.DataFrame(data)
#     data1.columns = ["vin", "driverD", "passD", "rrD", "rlD"]
#     return data1
#
#
# '''
# 电源各模式时长统计
# '''
#
#
# def systemMode():
#     sql = '''
#     select vin,
#            sumIf(runningDifferenceStartingWithFirstValue(tid) as tid_diff,
#                system_power_mode=1 and tid_diff <= 120000 and tid_diff > 0)/1000 as accTime,
#            sumIf(runningDifferenceStartingWithFirstValue(tid) as tid_diff,
#                system_power_mode=2 and tid_diff <= 120000 and tid_diff > 0)/1000 as onTime,
#            sumIf(runningDifferenceStartingWithFirstValue(tid) as tid_diff,
#                system_power_mode=3 and tid_diff <= 120000 and tid_diff > 0)/1000 as crackTime
#     from
#     chb121_glgd_loc
#     group by vin
#     '''
#     data = client.execute(sql)
#     return data
#
#
# '''
# 行程划分
# '''
#
#
# def trips():
#     sql = '''
#     select vin, toDateTime(tid/1000)as time, abs(runningDifferenceStartingWithFirstValue(tid)/1000) as time_diff,
#     (if(SystemPowerMode = 2, 1, 0) and if(time_diff>900, SystemPowerMode = 0, SystemPowerMode=SystemPowerMode)) as trans_sys,
#     runningDifferenceStartingWithFirstValue(trans_sys) as sys_diff,
#     if(sys_diff= -1, 0, sys_diff) as win,
#     sum(win) over (partition by vin order by tid) tripId
#     from p3011_loc
#     limit 100000
#     Settings allow_experimental_window_functions = 1;
#     '''
#     data = client.execute(sql)
#     return data
#
#
# '''
# 统计查询车辆的总数
# '''
#
#
# def carNums():
#     sql = '''
#         select
#             count() from (select distinct(vin) from f7x_loc)
#     '''
#     data = client.execute(sql)
#     nums = data[0][0]
#     return nums
#
#
# '''
# 车辆经纬度的查询，用于绘制车辆位置惹力图
# '''
#
#
# def carMap():
#     sql = '''
#     select
#        vin,
#        date,
#        lat,
#        lon,
#        vehicle_spd,
#        eng_spd,
#        tripId
#        from(
#         select generateUUIDv4() as uid,
#        vin,
#        toDateTime(tid / 1000) as date,
#        runningDifferenceStartingWithFirstValue(tid)/1000  as tid_diff,
#        tid_diff>900 as w,
#        sum(w) over(partition by vin order by tid) tripId,
#        lat,
#         lon,
#        vehicle_spd,
#        eng_spd
#         from chb121_glgd_loc
#         where vin='LGWEF5A50JH600734'
#         Settings allow_experimental_window_functions = 1)
#         ;
#     '''
#     # 执行语句并赋给列名，生成DataFrame
#     data = client.execute(sql)
#     df = pd.DataFrame(data)
#     df.columns = ['vin', 'date', 'lat', 'lon', 'vehicle_spd', 'eng_spd', 'tripId']
#     return df
