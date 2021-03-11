# 生成rss.xml到web目录


def 生成rss文件(文件名, 电费余额):
    template = '<?xml version="1.0" encoding="UTF-8" ?><rss version="2.0"><channel><title>电费查询(' + 文件名 + ')</title><link>https://mydw.xyz</link><description>曹伟nmsl</description><item><title>' + 文件名 + '剩余电费为：' + str(电费余额) + '</title><link>https://mydw.xyz</link><description>曹伟nmsl</description></item></channel></rss>'
    with open('./xml/' + 文件名 + '.xml', 'w', encoding='utf-8') as f:
        f.write(template)
