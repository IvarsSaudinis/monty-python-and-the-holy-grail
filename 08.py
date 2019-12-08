# Pārveidot 11.nodaļas mušmiru piemēru par Python3 programmu
from classes import apriori

dataset = [line.split() for line in open('data/agaricus-lepiota.data').readlines()]

L, suppData= apriori.apriori(dataset, minsupport=0.3)

for item in L[1]:
    if item.intersection('2'):
        print (item)
#large
for item in L[6]:
    if item.intersection('2'):
        print (item)
