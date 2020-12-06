import os

file_name = os.listdir("C:\\Users\\Hitesh bhargav\\PycharmProjects\\ApiTestingwithPython\\Test_data")

# Without list comprehension

for i in file_name:
    if i.__contains__(".txt") and i.__contains__("Error"):
        print(i)

# With list comprehension

file_filter = [i for i in file_name if i.__contains__(".txt") and i.__contains__("Error")]
print(file_filter)

