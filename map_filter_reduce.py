def square(x):
    return x*x
nums=[1,2,3,4,5]
squares=list(map(square,nums))
print(squares)


def is_even(x):
    return x%2==0
num2=[1,2,3,4,5]
evens=list(filter(is_even,num2))
print(evens)


#####
from functools import reduce
num1=[1,2,3,4,5,6]
def multiply(x,y):
    return x*y
product=reduce(multiply,num1)
print(product)


