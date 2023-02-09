for i in range(151):
    print(i)
for i in range(5, 1000, 5):
    print(i)
for i in range(1, 101):
    if (i % 10 == 0):
        print("Coding Dojo")
    elif (i % 5 == 0):
        print("Coding")
    else: print(i)
def odd(start, end):
    sum = 0
    for i in range(start, end):
        if (i % 2 != 0):
            sum += int(i)
    return sum
print(odd(0,500000))
for i in range(2018, 0, -4):
    if (i % 2 == 0):
        print(i)
def multiples_of_x(low, high, mult):
    for i in range(low, high+1):
        if (i % mult == 0):
            print(i)
multiples_of_x(2, 9, 3)