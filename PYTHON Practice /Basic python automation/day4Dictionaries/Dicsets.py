#Dictionary basics
User={
    "name" : "Rahul",
    "age" : 26,
    "its_admin": False
}
print(User["name"])
User["location"]="'Jamshedpur"
print(User)

# Loop thought dictionary
for key, value in User.items():
    print(f"{key}:{value}")

#delete key
del User["age"] 

#sets
unique_num = {1,2,3,1,2,4}
print(unique_num)

unique_num.add(5)
print(unique_num)