#To Add

list1=[1,2,3,4,5,6]

list2=["A","B","C","D"]

list3=["hELLO",1,True,40.55]

list4=[1,[2,3,4],5,6]

print("insert")
list1.insert(len(list1), 7)
print(list1)

print("append")
list1.append(8)
print(list1)

#extend
print("extend")
list1.extend([9,10,11])
print(list1)
#To Remove

list1.pop(1)

print("pop")
print(list1)

#del
print("del")
del list1[3]


print(list1)
print(*list1)
print(list1,sep="")
for x in list1:
    print(x,end="")
