a=int(input("Enter the number of elements you want to enter"))
l1=[]
sum=0
for i in range(0,a):
    num=int(input("Enter the elements"))
    l1.append(num)
    
for i in l1:    
    sum=sum+i
      
print("sum of number is ",sum)