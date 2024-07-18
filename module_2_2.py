first = int(input("число 123: "))
second = int(input("число 456: "))
third = int(input("число 789: "))

if first == second == third:
    print(3)
else:
    if first == third or first == second:
        print(2)
    if first != second != third:
        print(0)


first = int(input("число 42: "))
second = int(input("число 69: "))
third = int(input("число 42: "))

if first == second == third:
    print(3)
else:
    if first == third or first == second:
        print(2)
    if first != second != third:
        print(0)