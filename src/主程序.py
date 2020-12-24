import 查电费
import 生成rss
import time

if __name__ == "__main__":
    rooms = ["B101", "B102", "B219"]
    余额字典 = {
        "B101" : "", 
        "B102" : "", 
        "B219" : ""
    }
    while True:
        for roomID in rooms:
            电费余额 = 查电费.获取电费json(roomID)
            if 余额字典[roomID] != 电费余额:
                余额字典[roomID] = 电费余额
                生成rss.生成rss文件(roomID, 电费余额)
            time.sleep(0.1)
        time.sleep(1)
