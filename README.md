# Tickets_Master

· 本项目参考自实验楼文档 并由本人使用python3.5版本独立完成

    Usage:
        python tickets.py [-dgktz] <from> <to> <date>
    
    Options:
        -d              动车
        -g              高铁
        -k              快速
        -t              特快
        -z              直达
    Options默认为全选

# 可能需要手动添加的库:
     pip install requests,pprint,docopt,prettytable

· 数据由查询12306火车票返回json获取，通过分析其数据内容，将车次信息打印至屏幕中，对其输出仍需美化

· 对data暂时还没有做出处理，需按照 year-mouth-day 如 2018-05-01的格式进行输入，否则会出现Json读取错误


