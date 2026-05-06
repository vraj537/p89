import sys

print(sys.argv[0])
print(sys.argv[1])
print(sys.argv[2])

sum=int(sys.argv[1])+int(sys.argv[2])#argument vector

print("sum of argv[1] and srgv[1] ",sum)

s=0
for x in range(1,len(sys.argv)):
    s=s+int(sys.argv[x])
    
    
print("sum of all arguments is ",s) 