import 查电费
import 生成rss

from 汉语模组 import *

if __name__ == "__main__":
    房间们 = ["B101", "B102", "B219", "B309", "B524", "B424"]
    余额字典 = 迪克森.来自关键(房间们, 0)
    while True:
        for 房间编号 in 房间们:
            已经有的数据 = 余额字典.拿(房间编号)
            余额 = 查电费.获取电费json(房间编号, 已经有的数据)
            余额字典.放(房间编号, 余额)
            生成rss.生成rss文件(房间编号, 余额字典.拿(房间编号))
            休息(0.1)
        休息(600)

