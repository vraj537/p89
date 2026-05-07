from array import *

arr1=array('i',[11,22,33,44,55])

for i in arr1:
    print(i)

for i in range(len(arr1)):
    print(f"Element at {i}={arr1[i]}")

print()
print()
arr1[2]=800

for i in range(len(arr1)):
    print(f"Element at {i}={arr1[i]}")

print()
