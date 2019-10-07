user_info = {
    'name' : 'Shivam Bhargava',
    'age' : 26,
    'mob' : 1234567890,
    'm_name' : "Kusum Bhargav",
    'f_name' : "Ved Prakash Bhargav"

}

#Check values methds
#if 26 in user_info.values():
#    print("present")

#find all values
#for i in user_info.values():
#    print(i)

#user_info_values = user_info.values()
#print(user_info_values)

#user_info_key = user_info.keys()
#print(user_info_key)

#items method

#user_items = user_info.items()
#print(user_items)

for key, value in user_info.items():
    print(f"keys is {key} and values is {value}")