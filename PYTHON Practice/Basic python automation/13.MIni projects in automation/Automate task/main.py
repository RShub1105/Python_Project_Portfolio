def clean_name(name):
    return name.strip().capitalize()

def main():
    with open("Name.txt","r", encoding="utf-8") as f :
        names= f.readlines()
    print("Raw names from file:", names)
    names = [name for name in names if name.strip()]
    print("After filtering empty lines:", names)
    cleaned_names = [clean_name(name)for name in names]
    print("Cleaned names:", cleaned_names)


    with open("cleaned_name.txt","w", encoding="utf-8") as f:
        for name in cleaned_names:
            f.write(name + "\n")

    print(f"{len(cleaned_names)} name processed!")
    
if __name__ == "__main__":
    main()
  
      