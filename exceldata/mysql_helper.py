# -*- coding: utf-8 -*-

import pymysql.cursors

config = {
    'host': 'rdsd0lsl99tpbjn55fp5o.mysql.rds.aliyuncs.com',
    'port': 3306,
    'user': 'qicaip',
    'passwd': 'qicai_123_p',
    'db': 'prod_qicai',
    'charset': 'utf8mb4'
}


def query_one(sql, params):
    """查询单条记录"""
    # 连接数据库
    connect = pymysql.Connect(**config)
    try:
        with connect.cursor() as cursor:
            # 执行查询
            cursor = cursor.execute(sql, params)
            result = cursor.fetchone()
            return result
    finally:
        # 关闭连接
        cursor.close()
        connect.close()


def query_all(sql, params):
    """查询多条记录"""
    # 连接数据库
    connect = pymysql.Connect(**config)
    try:
        with connect.cursor() as cursor:
            # 执行查询
            cursor.execute(sql, params)
            result = cursor.fetchall()
            return result
    finally:
        # 关闭连接
        cursor.close()
        connect.close()


def del_many(sql, params):
    """删除多条记录"""
    # 连接数据库
    connect = pymysql.Connect(**config)
    try:
        with connect.cursor() as cursor:
            # 执行查询
            cursor.execute(sql, params)
            connect.commit()
            return cursor.rowcount
    finally:
        # 关闭连接
        cursor.close()
        connect.close()


def update_by_params(sql, params):
    """通过条件更新多条记录"""
    # 连接数据库
    connect = pymysql.Connect(**config)
    try:
        with connect.cursor() as cursor:
            # 执行查询
            cursor.execute(sql, params)

            connect.commit()
            return cursor.rowcount
    finally:
        # 关闭连接
        cursor.close()
        connect.close()


def update_many_by_params(sql, params):
    """通过条件执行多次更新,更新多条记录"""
    # 连接数据库
    connect = pymysql.Connect(**config)
    try:
        with connect.cursor() as cursor:
            # 执行查询
            cursor.executemany(sql, params)
            connect.commit()
            return cursor.rowcount
    finally:
        # 关闭连接
        cursor.close()
        connect.close()
