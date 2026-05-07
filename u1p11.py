l1=[1,2,3,4,5]
print(l1)
target=int(input("Enter your target"))

for i in l1:
    if i == target:
        print(f"{target} found in the list")
        break
else:
    print("Target not Found in the list")

    
