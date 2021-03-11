import 查电费
import 生成rss
import time

if __name__ == "__main__":

    rooms = ["B101", "B102", "B219", "B309", "B524", "B424"]

    余额字典 = {}
    for roomID in rooms:
        余额字典[roomID] = 0

    while True:
        for roomID in rooms:
            余额字典[roomID] = 查电费.获取电费json(roomID, 余额字典[roomID])
            生成rss.生成rss文件(roomID, 余额字典[roomID])
            time.sleep(0.1)
        time.sleep(600)

