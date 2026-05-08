# USER CHOOSE NO: 01
# ASKING ABOUT LAGGAGE WEIGHT
weight = int(input("How much your laggage weight?"))

# USER CHOOSE NO: 02
# CONDITION FOR INTERNATIONAL OR EXPRESS SHIPPING
print("\n1. International\n"
      "2. Local\n")
choice = int(input("Choose any one of the above: "))

# USER CHOOSE NO: 03
# DELIVERY ACCORDING TO ITS TRANSPORT
print("\n1. Express\n"
      "2. Priority\n"
      "3. Standard\n")
delivery = int(input("Choose any one of the above:"))

# USER CHOOSES INTERNATIONAL AND PROIRITY
if(choice == 1 and delivery == 1):
    print(f"\n20% surcharge for Internationall shipping.")
    print(f"Express will cost you $10")

    # CONDITIONS TO CHECK THE RATE ACCORDING TO WEIGHT
    if(weight < 5 ):
        rate = 5
        delivery_Charges = 10

        # EXTRA CHARGES FOR INTERNATIONAL SHIPPING
        total = (20 * rate) / 100 
        print(f"The rate is ${rate + total + delivery_Charges}.")

    elif(weight >= 5 and weight <= 20):
        rate = 15
        delivery_Charges = 10

        # EXTRA CHARGES FOR INTERNATIONAL SHIPPING
        total = (20 * rate) / 100 
        print(f"The rate is ${rate + total + delivery_Charges}.")

    elif (weight > 20):
        rate = 30
        delivery_Charges = 10

        # EXTRA CHARGES FOR INTERNATIONAL SHIPPING
        total = (20 * rate) / 100 
        print(f"The rate is ${rate + total + delivery_Charges}.")

# USER CHOOSES INTERNATIONAL AND PROIRITY
elif (choice == 1 and delivery == 2):
    print(f"20% surcharge for Internationall shipping.\n")
    print(f"Priority will cost you $20")

    # CONDITIONS TO CHECK THE RATE ACCORDING TO WEIGHT
    if(weight < 5 ):
        rate = 5
        delivery_Charges = 20

        # EXTRA CHARGES FOR INTERNATIONAL SHIPPING
        total = (20 * rate) / 100 
        print(f"The rate is ${rate + total + delivery_Charges}.")

    elif(weight >= 5 and weight <= 20):
        rate = 15
        delivery_Charges = 20

        # EXTRA CHARGES FOR INTERNATIONAL SHIPPING
        total = (20 * rate) / 100 
        print(f"The rate is ${rate + total + delivery_Charges}.")

    elif (weight > 20):
        rate = 30
        delivery_Charges = 20

        # EXTRA CHARGES FOR INTERNATIONAL SHIPPING
        total = (20 * rate) / 100 
        print(f"The rate is ${rate + total + delivery_Charges}.")

# USER CHOOSES INTERNATIONAL AND STANDARD
elif (choice == 1 and delivery == 3):
    print(f"20% surcharge for Internationall shipping.\n")
    print(f"Standard delivery is free.")

    # CONDITIONS TO CHECK THE RATE ACCORDING TO WEIGHT
    if(weight < 5 ):
        rate = 5

        # EXTRA CHARGES FOR INTERNATIONAL SHIPPING
        total = (20 * rate) / 100 
        print(f"The rate is ${rate + total}.")

    elif(weight >= 5 and weight <= 20):
        rate = 15

        # EXTRA CHARGES FOR INTERNATIONAL SHIPPING
        total = (20 * rate) / 100 
        print(f"The rate is ${rate + total}.")

    elif (weight > 20):
        rate = 30

        # EXTRA CHARGES FOR INTERNATIONAL SHIPPING
        total = (20 * rate) / 100 
        print(f"The rate is ${rate + total}.")

else:
     # USER CHOOSES lOCAL AND EXPRESS
    if(choice == 2 and delivery == 1):
        print(f"Local shipping is free.\n")
        print(f"Express will cost you $10")

        # CONDITIONS TO CHECK THE RATE ACCORDING TO WEIGHT
        if(weight < 5 ):
            rate = 5
            delivery_Charges = 10

            print(f"The rate is ${rate + delivery_Charges}.")

        elif(weight >= 5 and weight <= 20):
            rate = 15
            delivery_Charges = 10

            print(f"The rate is ${rate + delivery_Charges}.")

        elif (weight > 20):
            rate = 30
            delivery_Charges = 10

            print(f"The rate is ${rate + delivery_Charges}.")

    # USER CHOOSES INTERNATIONAL AND PROIRITY
    elif (choice == 1 and delivery == 2):
        print(f"Local shipping is free.\n")
        print(f"Priority will cost you $20")

        # CONDITIONS TO CHECK THE RATE ACCORDING TO WEIGHT
        if(weight < 5 ):
            rate = 5
            delivery_Charges = 20

            print(f"The rate is ${rate + delivery_Charges}.")

        elif(weight >= 5 and weight <= 20):
            rate = 15
            delivery_Charges = 20

            print(f"The rate is ${rate + delivery_Charges}.")

        elif (weight > 20):
            rate = 30
            delivery_Charges = 20

            print(f"The rate is ${rate + delivery_Charges}.")

    # USER CHOOSES LOCAL AND STANDARD
    elif (choice == 2 and delivery == 3):
        print(f"Local shipping is free.\n")
        print(f"Standard delivery is free.")

        # CONDITIONS TO CHECK THE RATE ACCORDING TO WEIGHT
        if(weight < 5 ):
            rate = 5

            print(f"The rate is ${rate}.")

        elif(weight >= 5 and weight <= 20):
            rate = 15

            print(f"The rate is ${rate}.")

        elif (weight > 20):
            rate = 30
            
            print(f"The rate is ${rate}.")