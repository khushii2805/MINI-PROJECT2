# Smart Canteen Billing and Order Analyzer

print("Welcome to Smart Canteen")
total = 0
names = []
quantities = []
amounts = []
while True:
    print("\n----- MENU -----")
    print("1. Veg Sandwich - Rs.60")
    print("2. Masala Dosa - Rs.80")
    print("3. Chole Rice - Rs.90")
    print("4. Paneer Roll - Rs.100")
    print("5. Tea - Rs.20")
    choice = int(input("Select your item [1-5]:-"))

    if choice == 1:
        name = "Veg Sandwich"
        price = 60
    elif choice == 2:
        name = "Masala Dosa"
        price = 80
    elif choice == 3:
        name = "Chole Rice"
        price = 90
    elif choice == 4:
        name = "Paneer Roll"
        price = 100
    elif choice == 5:
        name = "Tea"
        price = 20
    else:
        print("Please select a valid item.")
        continue

    qty = int(input("Enter quantity: "))

    if qty <= 0:
        print("Please enter a valid quantity.")
        continue

    bill = price * qty
    total = total + bill

    names.append(name)
    quantities.append(qty)
    amounts.append(bill)

    print(name, "added successfully")
    print("Amount:-", bill)
    answer = input("Do you want anything else? (yes/no): ")

    if answer.lower() == "no":
        break
    elif answer.lower() == "yes":
        continue
    else:
        print("Invalid response. Ending order.")
        break

if total == 0:
    print("\nNo order placed.")
else:
    print("\n------ YOUR BILL ------")

    for i in range(len(names)):
        print(names[i], "x", quantities[i], "=", amounts[i])
    print("----------------------")
    print("Total amount:", total)
    if total >= 500:
        discount = total * 10 / 100
    elif total >= 250:
        discount = total * 5 / 100
    else:
        discount = 0
    final_bill = total - discount
    print("Discount:", discount)
    print("Final bill:", final_bill)

    print("\nThank you... Dubara Jarur Aaiyega.")

    
