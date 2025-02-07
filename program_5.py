#By: Sabria Fafach
#Date: Febuary 7, 2025
#Name: program_5.py

#This portion of the code finds the hot dog cost
hot_dog=input("Enter a kind of hot dog (Hot Dog or Chili Dog):")
if hot_dog=="Hot Dog":
    hot_dog_cost=3.50
else:
    hot_dog_cost=4.50

#This portion of the code finds the topping cost
topping=input("Enter a kind of topping (Cheese, Peppers, Grilled Onions, or none):")
if topping=="Cheese":
    topping_cost=0.50
elif topping=="Peppers":
    topping_cost=0.75
elif topping=="Grilled Onions":
    topping_cost=1.00
else:
    topping_cost=0

total_cost_wo_tax=hot_dog_cost+topping_cost
print(f"The total cost of your Hot Dog and your topping without tax is ${total_cost_wo_tax}.")

percent_tax=0.07

tax=total_cost_wo_tax*percent_tax
print(f"Your tax is ${tax:.2f}.")

total=tax+total_cost_wo_tax
print(f"Your total cost is ${total:.2f}.")