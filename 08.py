# Pārveidot 11.nodaļas mušmiru piemēru par Python3 programmu
from classes import apriori

mushDatSet = [line.split() for line in open('data/agaricus-lepiota.data').readlines()]

L,suppData=apriori.apriori(mushDatSet, minSupport=0.3)
for item in L[1]:
    if item.intersection('2'): print (item)
