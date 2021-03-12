# 生成rss.xml到web目录
from 汉语模组 import *

def 生成rss文件(文件名, 电费余额):
    模板 = '<?xml version="1.0" encoding="UTF-8" ?><rss version="2.0"><channel><title>电费查询(' + 文件名 + ')</title><link>https://mydw.xyz</link><description>曹伟nmsl</description><item><title>' + 文件名 + '剩余电费为：' + str(电费余额) + '</title><link>https://mydw.xyz</link><description>曹伟nmsl</description></item></channel></rss>'
    with 文件操作.打开('./可扩展标记语言/' + 文件名 + '.xml', 'w', encoding='utf-8') as 文件:
        文件操作.写(文件)(模板)
