
name = input("What is your name : ")
age = input("what is your age : ")
fav_mov = input("Your fav movies spreated by comma : ").split(",")
fav_song = input("Your fav song sprated by comma : ").split(",")

user = {}

user['name']= name
user['age']=age
user['fav_mov']=fav_mov
user['fav_song']=fav_song

for key, value in user.items():
    print(f"{key}:{value}")

