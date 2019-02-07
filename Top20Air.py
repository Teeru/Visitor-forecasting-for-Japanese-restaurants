#!/usr/bin/python
import sys
import csv
#define an empty dict
visit_dict = {}

reader = csv.reader(sys.stdin, delimiter = ',')

#--- get all lines from stdin ---
for line in reader:
    store_id , visit_date, visitors = line
    try:
        num_visit = int(visitors)
    except:
        continue
    try:
        visit_dict[store_id]+=num_visit
    except:
        visit_dict[store_id] = 0

#sort dictionary            
sorted_d = sorted(visit_dict.items(), key=lambda x: x[1], reverse = True)    
#print top 20 for the mapper
for i in range(20):
    print'%s\t%s'%(sorted_d[i][0],sorted_d[i][1])