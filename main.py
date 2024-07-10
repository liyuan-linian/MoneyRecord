import math
from Recoder import  Recoder

a = Recoder(123456)
a.renewDict()
a.addCost(2024,7,10,'吃晚饭',100,'')
print(a.Moneydict)

a.saveDict()