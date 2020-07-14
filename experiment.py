myList = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

s = []
for i in myList[:]:
    if i not in s:
        s.append(i)
    else:
        myList.remove(i)

print("The list with unique elements only:")
print(myList)
