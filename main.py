name = input("Enter name: ")

name_end_chr = name[len(name)-1]

if name_end_chr in "aeiou":
    age = int(input("Enter age: "))
    
    if age % 2 != 0:
        birth_year = int(input("Enter birth year: "))
        
        if birth_year % 2 != 0:
            print("You will be special next year.")
            
        else:
            print("Oh, you're still special")
    else: 
        print("Wow, you're special")
else:
    print("You're awesome!")

