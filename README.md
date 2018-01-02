# Tickets_Master

· 本项目参考自实验楼文档 并由本人使用python3.5版本独立完成

    Usage:
        tickets [-dgktz] <from> <to> <date>

    Options:
        -d              动车
        -g              高铁
        -k              快速
        -t              特快
        -z              直达

# 可能需要手动添加的库:
     pip install requests,pprint,docopt,prettytable

· 数据由查询12306火车票返回json获取，通过分析其数据内容，将车次信息打印至屏幕中

# To do
  ·做成一个图形界面，并在原基础上进行功能改善

  ·用户输入目的地，通过最短路找到其最方便的火车乘坐次序，并匹配发车及到站时间


