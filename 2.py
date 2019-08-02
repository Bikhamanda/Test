# import csv

# data = [
#     ['Andi','12345'], 
#     ['Budi','23456'], 
#     ['Caca','34567'],
#     ]
# # data = ['Andi','Budi','Caca']
# with open('fileku.csv', 'w', newline='') as x:
#     writer = csv.writer(x, delimiter='\\')
#     # for nama in data:
#     #     writer.writerow([nama])
#     # writer.writerows(data[1:])
#     for e in data:
#         writer.writerow(e)

# usia = 21

# print('Usia saya', usia)
# print('usia saya = {}'.format(usia))
# print(f'Usia saya = {usia}')

import csv
import json

# data = [
#     {'nama': 'Andi', 'nis' : 12345}, 
#     {'nama': 'Budi', 'nis' : 23456}, 
#     {'nama': 'Caca', 'nis' : 34567},
#     ]
# data = ['Andi','Budi','Caca']
# with open('test.csv', 'w', newline='') as x:
#     writer = csv.DictWriter(x, fieldnames=['nis', 'nama'])
#     writer.writeheader()
#     writer.writerows(data)

# data=[]
# with open('fileku.csv', 'r', newline='') as x:
#     reader = csv.DictReader(x)
#     for i in reader:
#         print(dict(i))
#         data.append(dict(i))
# print(data)