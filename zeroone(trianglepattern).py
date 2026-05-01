
number = 0
for i in range(1, 5 + 1):
    for j in range(i):
        print(number % 2, end="")
        number += 1
    print()