num = int(input(" Enter the Number:"))
if (num % 2) == 0:
    print("Even number")
else:
    print("odd number")

a = [1,2,3,4,5,6,7,8,9,10]
for val in a:
    if val % 2== 0:
        print(val,end=" ")