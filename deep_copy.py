import copy

list1 = [1,2,3,4]

#shallow copy
list2 = list1

print(id(list1))
print(id(list2))

list2.append(5)
print(list1)
print(list2)

#deep copy

list3 = copy.deepcopy(list1)
list3.append(6)
print(list3)
print("--Original list is--")
print(list1)