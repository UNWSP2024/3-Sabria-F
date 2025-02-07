#By: Sabria Fafach
#Date: Febuary 7, 2025
#Name: program_2.py

#Program #3: Shipping Charges
weight=float(input("Enter the weight of your shipment in lbs:"))
if weight<=2:
    total_cost=1.50*weight
    print(f"The cost to ship your item is ${total_cost: .2f}.")
elif weight>2 and weight<=6:
    total_cost=3.00*weight
    print(f"The cost to ship your item is ${total_cost: .2f}.")
elif weight>6 and weight<=10:
    total_cost=4.001*weight
    print(f"The cost to ship your item is ${total_cost: .2f}.")
else:
    total_cost=4.75*weight
    print(f"The cost to ship your item is ${total_cost: .2f}.")