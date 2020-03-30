
name = input("Enter aplphabet to check palindrome: ")
palindrome_name = name[-1::-1]


def camparesion ():

    if name == palindrome_name:
        return True
    else:
        return False

print(camparesion())


def is_palindrome(name):
    if name[::-1] == name:
        return True
    return False
print(is_palindrome(name))
print(is_palindrome("shivam"))