# USER CHOOSE : 01
weight = int(input("How much your laggage weight?"))

# WEIGHT RATE
if weight > 0 and weight < 5:
    rate = 5

elif weight >= 5 and weight <= 20:
    rate = 15

else:
    rate = 30

# USER CHOOSE : 02
print("\n1. International"
      "\n2. Local\n")
choice = int(input("Choose any of the above: "))

# DELIVERY CHARGES
if choice == 1:
    delivery_charges = (rate * 20) / 100
    print(f"International shipping will cost you ${delivery_charges}")

elif choice == 2:
    delivery_charges = 0
    print("Local shipping is free.")

else:
    print("Invalid input for shipping.")
    exit()

# USER CHOOSE : 03
print("\n1. Priority"
      "\n2. Express"
      "\n3. Standard")
transport = int(input("How would you like to transport your laggage? "))

if transport == 1:
    transport_charges = 20
    print(f"Priority transport will cost you ${transport_charges}")

elif transport == 2:
    transport_charges = 10
    print(f"Express transport will cost you ${transport_charges}")

elif transport == 3:
    transport_charges = 0
    print("Standard transport is free.")

else:
    print("Invalid input for transport.")
    exit()

total = rate + delivery_charges + transport_charges

print(f"Total rate is ${total}")