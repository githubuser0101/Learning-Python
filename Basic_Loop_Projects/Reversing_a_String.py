
# * Reversing a string
str = "Hannah" 
revStr = ""
for i in str:
    revStr = i + revStr

print(revStr)

# * Reversing a list
list = [1, 2, 3, 4, 5]
# list.reverse()
# print(list[-len(list):])

list2 = []
length = len(list)
while(length):
    list2.append(list[length-1])
    length-= 1
    # list2.append(list.pop())

print(list2)