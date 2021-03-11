import 查电费
import 生成rss
import time

if __name__ == "__main__":
    房间们 = ["B101", "B102", "B219", "B309", "B524", "B424"]
    余额字典 = dict.fromkeys(房间们, 0)
    while True:
        for 房间编号 in 房间们:
            余额字典[房间编号] = 查电费.获取电费json(房间编号, 余额字典[房间编号])
            生成rss.生成rss文件(房间编号, 余额字典[房间编号])
            time.sleep(0.1)
        time.sleep(600)

