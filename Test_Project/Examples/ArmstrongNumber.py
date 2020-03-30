
numrange = int(input("Enter number : "))

for i in range(numrange):
    num = i
    result = 0
    n = len(str(i))

    while (i != 0):
        digit = i % 10
        print(digit)
        result = result+ digit**n
        print(result)
        i = i //10
        print(i)

        if num == result:
            print(num)

