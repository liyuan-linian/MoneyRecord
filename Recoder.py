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
        with open(s, 'w') as file:
            json.dump(Moneydict, file, sort_keys=True, indent=4)

    def renewDict(self):
        s = "{id}.json".format(id=self.id)
        with open(s,'r') as file:
            self.Moneydict = json.load(file)

    def saveDict(self):
        s = "{id}.json".format(id=self.id)
        with open(s, 'w') as file:
            json.dump(self.Moneydict, file, sort_keys=False, indent=4)

    def addCost(self, year, month, day, type, count, notes):
        try:
            self.Moneydict[year]

        except:
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
                self.Moneydict[year].setdefalut(month,Temp_dict_month)

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
                    no = len(self.Moneydict[year][month][day]) + 1
                    Temp_dict_no = {
                        no: {
                            'type': type,
                            'count': count,
                            'notes': notes
                        }
                    }
