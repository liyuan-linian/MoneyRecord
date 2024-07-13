import math
from Recoder import  Recoder

a = Recoder(123456)
a.renewDict()
# + for spend and - for earnings

#a.addCost(2024,7,10,'吃晚饭',100,'')
a.delCost(2024,7,10,4)
a.saveDict()

print(a.getSum_day(2024,7,10))

a.saveDict()