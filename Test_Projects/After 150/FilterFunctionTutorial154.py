number = [1,2,3,3,4,4,5,6,7,12,14,32,4,6,9,876,]

# filter function
#def is_even(a):
#    return a%2==0

#even = tuple(filter(is_even,number))
#print(even)

# With lamda function

even = tuple(filter(lambda a:a%2==0,number))
print(even)


# list comprihance

new_even = [i for i in number if i%2==0]
print(new_even)