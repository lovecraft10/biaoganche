import sqlalchemy
from clickhouse_sqlalchemy import make_session
from sqlalchemy import Table, Column, Integer, String, DateTime, BIGINT, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, MetaData, literal, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
import pymysql

# 数据库连接配置相关
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

'''
一些数据库表的映射类
'''


# 借用台账
class StandingBook(Base):
    __tablename__ = 'standing_book'
    id = Column(BIGINT, primary_key=True)
    car_id = Column(BIGINT, index=True)
    cyy = Column(VARCHAR(255))
    depart = Column(VARCHAR(255))
    operator = Column(VARCHAR(255))
    mobile_phone = Column(VARCHAR(255))
    project_name = Column(VARCHAR(500))
    begin_date = Column(DateTime)
    end_date = Column(DateTime)
    give_back = Column(Integer())

    def to_dict(self):
        columns = self.__table__.columns.keys()
        result = {}
        for key in columns:
            if key == 'tid':
                value = getattr(self, key).strftime("%Y-%m-%d %H:%M:%S")
            else:
                value = getattr(self, key)
            result[key] = str(value)
        return result


# 故障台账
class CarFault(Base):
    __tablename__ = 'car_fault'
    id = Column(BIGINT, primary_key=True)
    car_id = Column(BIGINT, index=True)
    fault_describe = Column(VARCHAR(1000))
    create_by = Column(BIGINT)
    create_time = Column(DateTime)
    update_by = Column(BIGINT)
    update_time = Column(DateTime)

    def to_dict(self):
        columns = self.__table__.columns.keys()
        result = {}
        for key in columns:
            if key == 'tid':
                value = getattr(self, key).strftime("%Y-%m-%d %H:%M:%S")
            else:
                value = getattr(self, key)
            result[key] = str(value)
