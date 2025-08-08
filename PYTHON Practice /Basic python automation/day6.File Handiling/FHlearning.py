# Open and read
file = open("test.txt","r")
content= file.read()
print(content)
file.close()

# Write a file (create file if not exist)
file = open("test.txt","w")
file.write("Hello this is my first file.\n")
file.write("Adding another line.\n")
file.close()

#Append data.
file =open("test.txt","a")
for line in file:
    print(line.strip())
    file.close()

#read line by line.
file=open("text.txt","r")
for line in file:
    print(line.strip())
    file.close()

#Better way_with Block(auto close).
with open("test.txt","r")as file:
    print(file.read()) 