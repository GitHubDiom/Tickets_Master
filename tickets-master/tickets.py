'''
Usage:
    tickets [-dgktz] <from> <to> <date>

Options:
    -h  --help      查看帮助
    -d              动车
    -g              高铁
    -k              快速
    -t              特快
    -z              直达


'''
from docopt import docopt
import urllib3
urllib3.disable_warnings()

import requests
import stations
from prettytable import PrettyTable


class TrainsInfo(object):
    headers = '车次 车站 时间 历时 一等座 二等座 软卧 硬卧 软座 硬座 无座'.split()

    def __init__(self,raw_trains,options):
        self.raw_trains=raw_trains
        self.options=options

    def get_from_to_station_name(self,data_list):
        from_station_telecode=data_list[6]
        to_station_telecode=data_list[7]
        return '\n'.join(
        [
        stations.get_name(from_station_telecode),
        stations.get_name(to_station_telecode)
        ]
    
        )
    def get_start_arrive_time(self,data_list):
        return '\n'.join(
        [
            data_list[8],
            data_list[9]

        ]
    
        )
    def need_print(self,data_list):
        station_train_code=data_list[3]
        initial=station_train_code[0].lower()
        return (not self.options  or initial in self.options)

    def parse_train_data(self,data_list):
        return {
            'station_train_code': data_list[3],
            'from_to_station_name': self.get_from_to_station_name(data_list),
            'start_arrive_time': self.get_start_arrive_time(data_list),
            'lishi': data_list[10],
            'first_class_seat': data_list[31] or '--',
            'second_class_seat': data_list[30] or '--',
            'soft_sleep': data_list[23] or '--',
            'hard_sleep': data_list[28] or '--',
            'soft_seat': data_list[24] or '--',
            'hard_seat': data_list[29] or '--',
            'no_seat': data_list[33] or '--'
        }


    @property
    def trains(self):
        for train in self.raw_trains:
            data_list = train.split('|')
            if self.need_print(data_list):
                yield self.parse_train_data(data_list).values()

    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.headers)
        for train in self.trains:
            #print(train)
            pt.add_row(train)
        print(pt)

class TrainsCheck(object):
    url=(
    'https://kyfw.12306.cn/otn/leftTicket/query?'
    'leftTicketDTO.train_date={}&'
    'leftTicketDTO.from_station={}&'
    'leftTicketDTO.to_station={}&'
    'purpose_codes=ADULT'
        )    
    def __init__(self):
        self.arguments = docopt(__doc__)
        #print(self.arguments)
        self.from_station = stations.get_telecode(self.arguments['<from>'])
        self.to_station  = stations.get_telecode(self.arguments['<to>'])    
        self.date = self.arguments['<date>']
        #print(self.arguments.items())
        self.options = ''.join([key for key, value in self.arguments.items() if value is True])    
    
    @property
    def request_url(self):
        return self.url.format(self.date , self.from_station, self.to_station)
    
    #2018-04-28
    def run(self):
        #print(self.request_url)
        r= requests.get(self.request_url,verify=False)
        #print(r.json())
        trains = r.json()['data']['result']
        TrainsInfo(trains,self.options).pretty_print()

if __name__ == '__main__':
    TrainsCheck().run()