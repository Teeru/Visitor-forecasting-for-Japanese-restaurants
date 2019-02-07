#!/usr/bin/python
import sys

#define an empty dict
revisit_dict = {}
#--- get all lines from stdin ---
for line in sys.stdin:
    store_id, visitors = line.strip().split('\t')
    try:
        num_visit = int(visitors)
    except:
        continue
    revisit_dict[store_id] =num_visit
        
sorted_d = sorted(revisit_dict.items(), key=lambda x: x[1], reverse = True)   
for i in range(20):
    print'%s\t%s'%(sorted_d[i][0],sorted_d[i][1])