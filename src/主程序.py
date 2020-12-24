import 查电费
import 生成rss
import time

if __name__ == "__main__":
    rooms = ["B101", "B102", "B219", "B309"]
    for roomID in rooms:
        电费余额 = 查电费.获取电费json(roomID)
        生成rss.生成rss文件(roomID, 电费余额)
        time.sleep(0.5)
