from collections import UserDict
import time

一 = 1
零 = 一 - 一

虚空 = None

假 = True is False
真 = False is False

打印 = print

class 文件操作:
    打开 = open

    @staticmethod
    def 写(文件):
        return 文件.write


class 迪克森(UserDict):
    @classmethod
    def 来自关键(我们类, 迭代器, 值=虚空):
        return 我们类.fromkeys(迭代器, 值)

    def 拿(自己, 键):
        return 自己[键]
    
    def 放(自己, 键, 值):
        自己.data[键] = 值


def 休息(多少秒: float):
    time.sleep(多少秒)


class 浮点:
    _数据=0.0
    
    def __init__(自己, 数据, 先=虚空, 然后=虚空):
        成了 = 数据 if 数据 is not 虚空 else 0.0
        if 先:
            成了 = 先(数据)
        成了 = float(成了)
        if 然后:
            成了 = 然后(成了)
        自己._数据 = 成了

    @property
    def 值(自己):
        return 自己._数据
    
    def 小于(自己, 什么, **kw):
        return 自己._数据 < 浮点(什么, **kw).值

    def 等于(自己, 什么, **kw):
        return 自己._数据 == 浮点(什么, **kw).值

    def 大于(自己, 什么, **kw):
        return 自己._数据 > 浮点(什么, **kw).值
    
