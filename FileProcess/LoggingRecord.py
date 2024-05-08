# _*_ coding:utf-8 _*_
# @Time:2024/4/29 15:56
# @Author:cui泡泡
# @File:logging.py
# @Software:PyCharm
import logging
from functools import wraps

# 设置日志记录器
logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s %(levelname)-8s %(message)s')


def log_and_error_handler(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            logging.info(f"{func.__name__} returned {result}")
        except Exception as e:
            logging.error(f"{func.__name__} failed with error: {e}")
        return result

    return wrapper