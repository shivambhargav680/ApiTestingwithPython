def longest_sublist(string):
    n = len(string)
    val1 = set()
    for i in range(0, n):
        val1.add(string[i])
    return val1,len(val1)

print(longest_sublist(input("Enter your string : ")))
