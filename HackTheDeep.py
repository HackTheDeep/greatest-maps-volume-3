#http://www.marinespecies.org/aphia.php?p=webservice&type=python

import csv
import psycopg2
import itertools
import sys
from fuzzywuzzy import fuzz


#Connect To Database
conn = psycopg2.connect(
   host='amnh-map-the-collections.c1bevxdyosto.us-east-1.rds.amazonaws.com',
   dbname="map_the_collection",
   user="amnhhackthedeep",
   password="amnhhackthedeep123!")


#Fetch Data
cur = conn.cursor()

ex = cur.execute("select distinct \"Family Name in Database\" from hackathon_2018_dirty_dataset_iz order by \"Family Name in Database\" asc")

nameList = cur.fetchall()


#Compare First String In Row Against Rest Of Strings In Same Row.
#Use Fuzzy Search To Lexically Analyse And Compare String Similarity, Use % Output To Correct Typo's  
nameList2 = nameList
nameList3 = []

for x in nameList:
    #setrecursionlimit(58000)
    for y in nameList2:
        diff = fuzz.token_sort_ratio(x,y)
        #if diff is not 100 then it could be a new family if diff is 100 probably typo
        if (x not in nameList3 and x != y and diff == 100):
            nameList3.append(x)
    print(x)
    print()


#Always Remember To Close Connections!
cur.close()
