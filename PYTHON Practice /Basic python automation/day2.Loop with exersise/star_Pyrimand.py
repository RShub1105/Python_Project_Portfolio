n = int(input("Enter the number:"))
for i in range (1,1+n):
    print(" " *(n-i),end="")
    print("*" * (2*i-n),end="")
    print()



