# 4 * 3 * 2 * 1

num = int(input("Enter number:"))
fact = 1
if num < 0:
    print(" Not a negative number:")
elif num == 0:
    print("0 is 1")
else:
    for i in range(1 , num+1):
        fact = fact*i
        print("fact of ",num,"is ",fact)

