try:
    num=float(input("Enter a number "))
    assert num>0,"number must be greater than zero"
    print("you have entered valid number")

except AssertionError as e:
    print("Assertion error ",e)
except ValueError as v:
    print("Value Error ",v)
