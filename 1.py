import csv

with open('Book2.csv', 'r') as fileku:
    baca = csv.reader(fileku)
    print(baca)
    # for x in baca:
        # print(x[0])
#         students.append(x[0])
# print(students)