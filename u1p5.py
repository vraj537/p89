l1=[1,2,3,4,5,6]
l2=[4,5,6,7,8,9]

common=[]
non_common=[]

for i in l1:
    if i in l2:
        common.append(i)

print(common)

for i in l1:
    if i not in l2:
        non_common.append(i)

for i in l2:
    if i not in l1:
        non_common.append(i)

print(non_common)

