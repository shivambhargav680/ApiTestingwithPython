#square = {f"Square of {num} is":num**2 for num in range(1,10)}
#for k,v in square.items():
    #print(f"{k}:{v}")


string = 'SHivam Bhargava'
word_count = {char:string.count(char) for char in string}
print(type(word_count))
print(word_count)
