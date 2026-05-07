import math

print("---Menu---")
print("(1)--Area of Circle--")
print("(2)--Area of Triangle--")
print("(3)--Area of Square--")
print("(4)--Simple Interest--")
print("(5)Exit--")

op=int(input("Enter the option"))

match(op):
    case 1:
        radius=float(input("Enter the Radius of Circle"))
        area=math.pi*radius*radius
        print(f"Area of circle is {area:.2f}")
    case 2:
        base=float(input("Enter the base of triangle"))
        height=float(input("Enter the height of triangle"))
        area=0.5*base*height
        print(f"Area of triangle is {area:.2f}")
    case 3:
        sq=float(input("Enter the side of square"))
        area=sq*sq
        print(f"Area of square is {area:.2f}")

    case 4:
        principal=float(input("Enter the principal amount"))
        rate=float(input("Enter rate of interest"))
        time=float(input("Enter the Time"))

        si=principal*rate*time/100

        print(f"Simple interest is {si:.2f}")

    case 5:
        print("Exit")



    
