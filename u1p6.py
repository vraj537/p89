a=int(input("Enter the first value"))
b=int(input("Enter the Second value"))

print("Memory Location of a is ",id(a))
print("Memory Location of b is ",id(b))



if a is b:
    print("both are same")
else:
    print("both are not same")

l1=[1,2,3,4,5]
l2=[1,2,3,4,5]

print("Memory location of list 1 ",id(l1))
print("Memory location of list 2 ",id(l2))

if l1 is l2:
    print("both have same location")
else:
    print("both doesn't have same location")
    
