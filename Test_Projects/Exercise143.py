def to_power(num, *args):
        if args:
            temp = []
            for i in args:
                temp.append(i**num)
            return temp
        else:
            return "You did not pass any value"

lst = [1,2,3]
print(to_power(2,*[]))

