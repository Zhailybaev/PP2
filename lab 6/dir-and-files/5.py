color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
with open('C:\\Users\\Asus\\Desktop\\pp2\\lab 6\\dir-and-files\\ex.txt', "w") as myfile:
        for c in color:
                myfile.write("%s\n" % c)

content = open("C:\\Users\\Asus\\Desktop\\pp2\\lab 6\\dir-and-files\\ex.txt")
print(content.read())