#By: Sabria Fafach
#Date: Febuary 5, 2025
#Name: program_2.py

age=int(input("Enter someone's age:"))

if age<=1:
    print(f"infant")

elif age>1 and age<13:
    print("child")

elif age>=13 and age<20:
    print("teenager")

else:
    print("adult")