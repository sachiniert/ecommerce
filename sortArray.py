li = [76,34,8,8,34,90]

for i in range(0, len(li)):
    for j in range(i+1, len(li)):
        if li[i] >=  li[j]:
            temp = li[i]
            li[i] = li[j]
            li[j] = temp
print(li)