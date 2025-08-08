#Create a file data.txt and write 5 line of text.
file = open("data.txt", "w")
file.write("Line 1:Hello this is my first file line.\n")
file.write("Line 2:I am learning the python code.\n")
file.write("Line 3:were right now I am in file handling.\n")
file.write("Line 4:It is very easy i can write as many as line as i want.\n")
file.write("Line 5:It is very important for Devops.")
file.close()
print("file created and written successfully!")

#read the file and print each line with line number.
file = open("data.txt","r")
content = file.read()
print("File content:\n",content)
file.close()

with open("data.txt","w")as file:
    file.write("your lines hear...\n")
    with open("data.txt","r")as file:
        print(file.read())

#append a new line.
import datetime
with open("data.txt","a") as file:
 file.write("This file was updated\n")
 print("New line appended")

# count how many words the file has in totals
with open("data.txt","r")as file:
   content = file.read()
   words = content.split()
   word_count = len(words)
print("Total words in file:",word_count)

# Make simple log writer using timestamp.

print(datetime.datetime.now())