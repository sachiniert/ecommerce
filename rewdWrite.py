file = open('test.txt')
#Read all the contents of file
# read n number of character by passing parameter
#print(file.read(5))

#read one single line at a time readLine()
print(file.readline())
print(file.readline())

file.close()

#print line by line using readLine method
line = file.readline()
while