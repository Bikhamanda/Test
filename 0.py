myFile = open("Book2.csv", "r")
# print(myFile.readlines())

data = ["Budi", "Caca","Didi Kempot" ]
myFile =open('Book2.csv', 'a')
# myFile.write('Andi')
for i in data :
    myFile.write('\n' + i)

myFile = open('Book2.csv', 'r')
print(myFile.readlines())

