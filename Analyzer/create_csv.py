import pickle
import csv
import json
import os

with open('result.pickle', 'rb') as handle:
    a = pickle.load(handle)

with open('result1.pickle', 'rb') as handle:
    b = pickle.load(handle)

with open('result2.pickle', 'rb') as handle:
    c = pickle.load(handle)

d={}
v={}
for i in a:
	if i in b and float(b[i][0])>0.0 and float(b[i][1])>0.0 and a[i].days>0:
		m=[a[i].days]
		m.append(float(b[i][0]))
		m.append(float(b[i][1]))
		d[i]=m
m=[]
for i in d:
	if i in c and c[i]>0:
		m=[c[i]]
		m.append(d[i][0])
		m.append(d[i][1])
		m.append(d[i][2])
		v[i]=m

print(len(v))

with open('mycsvfile.csv','w') as f:
	writer = csv.writer(f, delimiter=',')
	writer.writerow(['repo_name', 'depth','timelag','complexity','nloc'])
	for i in v:
		row=[i]
		row.extend(v[i])
		writer.writerow(row)
			

