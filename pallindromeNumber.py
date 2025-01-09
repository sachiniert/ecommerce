# 121 =121
# 212 = 212
num = int(input("Enter a number:"))
tem = num
rev = 0
while (num > 0):
    dig = num % 10
    rev = rev*10 + dig
    num = num//10
if(tem == rev):
        print("Palindrome number")
else:
        print("Not a Pallindrome number")