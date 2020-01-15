# -*- coding: utf-8 -*-
'''
@author: liww liww@cenboomh.com
@file: date_G.py
@time: 2020/1/9 15:40
@desc:
'''
import calendar
import datetime
import pandas as pd


class Datadis():

    def set_strdate(self, strstring):
        """
        读取字符串时间
        :param strstring: 2020-1-9 or 2020:1:9 or 20200109
        :return:
        """
        date_list = []
        strstring = str(strstring)
        if strstring.find('-'):
            date_list = strstring.split('-')
        elif strstring.find(':'):
            date_list = strstring.split(':')
        else:
            date_list[0], date_list[1], date_list[2] = strstring[:4], strstring[4:6], strstring[6:]

        self.year, self.month, self.day = date_list[0], date_list[1], date_list[2]

    def get_int_md(self):
        """
        获取月天数
        :return:
        """
        if self.year == None or self.month == None:
            today = datetime.datetime.today()
        else:
            today = datetime.datetime(int(self.year), int(self.month), 1)
        month_n = calendar.monthrange(today.year, today.month)[1]
        return month_n

    def get_interval_vacation(self, start_date, end_date):
        """
        获取时间段内的双休日
        :param start_date:
        :param end_date:
        :return:
        """
        interval_date = []
        appointed_day_vacation = {'vacation': []}

        for x in list(pd.date_range(start=start_date, end=end_date)):
            interval_date.append(x)

        for appointed_day in interval_date:
            if appointed_day.weekday() == 5 or appointed_day.weekday() == 6:
                switch_day = datetime.date(appointed_day.year, appointed_day.month, appointed_day.day)
                appointed_day_vacation['vacation'].append(switch_day)

        appointed_day_vacation['total'] = len(interval_date)