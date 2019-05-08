import requests
import json
import pandas as pd
import csv

lnk = 'http://www.top500.org/list/2018/06/?page='
fileName = 'pt'
list_ = []
for pageID in range(1, 6):
    newLink = lnk + str(pageID)

    pageRead = pd.read_html(newLink, header=1)
    pageRead[0].to_csv(fileName + str(pageID) + '.csv', header=False, index=False)

f = csv.writer(open('out.csv', 'w'))
f.writerow(["Rank", "Site", "System", "Cores", "Rmax (TFlop/s)", "Rpeak (TFlop/s)", "Power (kW)"])
f = open("out.csv", "a")
for num in range(1, 6):
    for line in open("pt" + str(num) + ".csv"):
        f.write(line)
f.close()