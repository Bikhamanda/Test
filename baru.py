import json
import csv

data=[]

with open('data.json') as x:
    data = json.load(x)
    data.append(dict(x))

print(data)
data=[]
with open('data1.csv', 'w', newlines='') as y:
    writer = csv.DictWriter(y, fieldnames= ["nama","usia"])
    writer.writeheader()
    writer.writerows(y)

# with open('data1.json') as a :
#     reader = json.DictReader(a)
#     for i in reader:
#         data.append(dict(i))

# with open('data3.json','w', newline='') as z:
#     b = str(data)
#     z.write(b.replace("'",'"'))