import json


class Recoder():
    def __init__(self, id):
        self.id = id
        self.Moneydict = None
        s = "{id}.json".format(id=id)
        Moneydict = {
            1990: {  # year
                1: {  # month
                    1: {  # day
                        1: {  # no.1
                            'type': '生活支出',
                            'count': 100,
                            'notes': '买早饭'
                        },
                        2: {
                            'type': '娱乐服务',
                            'count': 100,
                            'notes': '充值游戏'
                        }
                    }
                }
            }
        }
        try:
            with open(s, 'x') as file:
                pass
        except:
            pass
        else:
            with open(s, 'w') as file:
                json.dump(Moneydict, file, sort_keys=True, indent=4)

    def renewDict(self):
        s = "{id}.json".format(id=self.id)
        with open(s, 'r') as file:
            self.Moneydict = json.load(file)

    def saveDict(self):
        s = "{id}.json".format(id=self.id)
        with open(s, 'w') as file:
            json.dump(self.Moneydict, file, sort_keys=False, indent=4)

    # 添加一条新的记账
    def addCost(self, year, month, day, type, count, notes):

        year = '{year}'.format(year=year)
        month = '{month}'.format(month=month)
        day = '{day}'.format(day=day)

        try:
            self.Moneydict[year]

        except Exception as e:
            print(e)
            Temp_dict_year = {
                month: {  # month
                    day: {  # day
                        1: {  # no.1
                            'type': type,
                            'count': count,
                            'notes': notes
                        }
                    }
                }
            }
            self.Moneydict.setdefault(year, Temp_dict_year)

        else:
            try:
                self.Moneydict[year][month]

            except:
                Temp_dict_month = {
                    day: {  # day
                        1: {  # no.1
                            'type': type,
                            'count': count,
                            'notes': notes
                        }
                    }
                }
                self.Moneydict[year].setdefalut(month, Temp_dict_month)

            else:
                try:
                    self.Moneydict[year][month][day]

                except:
                    Temp_dict_day = {
                        1: {  # no.1
                            'type': type,
                            'count': count,
                            'notes': notes
                        }
                    }
                    self.Moneydict[year][month].setdefault(day, Temp_dict_day)

                else:
                    no = str(len(self.Moneydict[year][month][day]) + 1)
                    Temp_dict_no = {
                        'type': type,
                        'count': count,
                        'notes': notes
                    }
                    self.Moneydict[year][month][day].setdefault(no, Temp_dict_no)

    def delCost(self, year, month, day, no):
        """
        主要完成两个工作：
        1.删除字典中对应的键对
        2.完成剩下的建对的编号更新
        """
        year = '{year}'.format(year=year)
        month = '{month}'.format(month=month)
        day = '{day}'.format(day=day)
        no0 = no
        count = 0
        no = '{no}'.format(no=no)

        del self.Moneydict[year][month][day][no]
        temp_list = list(self.Moneydict[year][month][day].items())


        for i in temp_list:
            if int(i[0]) > no0:
                self.Moneydict[year][month][day]['{no}'.format(no=no0 + count)] = \
                    self.Moneydict[year][month][day].pop('{no}'.format(no=int(i[0])))
                count += 1

    def changeCost(self,year,month,day,no):
        pass
    def getSum_day(self, *date):
        """
        输入日期 返回三个结果
        """
        sumMoney = 0
        spendMoney = 0
        earningsMoney = 0

        for i in self.Moneydict['{year}'.format(year=date[0])]['{month}'.format(month=date[1])][
            '{day}'.format(day=date[2])].values():
            if i["count"] > 0:
                spendMoney += i["count"]
            if i["count"] < 0:
                earningsMoney += i["count"]

        sumMoney = spendMoney - earningsMoney
        return spendMoney, earningsMoney, sumMoney

    def getSum_Month(self, *date):

        sumMoney = 0
        spendMoney = 0
        earningsMoney = 0

        for i in self.Moneydict['{year}'.format(date[0])]['{month}'.format(date[1])].values():
            for j in i.values:
                if j["count"] > 0:
                    spendMoney += j["count"]
                if j["count"] < 0:
                    earningsMoney += j["count"]

        sumMoney = spendMoney - earningsMoney
        return spendMoney, earningsMoney, sumMoney

    def getSum_year(self, *date):

        sumMoney = 0
        spendMoney = 0
        earningsMoney = 0

        for i in self.Moneydict['{year}'.format(date[0])].values():
            for j in i.values:
                for k in j.values:
                    if k["count"] > 0:
                        spendMoney += k["count"]
                    if k["count"] < 0:
                        earningsMoney += k["count"]

        sumMoney = spendMoney - earningsMoney
        return spendMoney, earningsMoney, sumMoney
