bank_records = {
    "1234567890": {"pin": "1963", "name": "Abiodun Praise", "balance": 50000},
    "7014775622": {"pin": "2030", "name": "Ajibola-Johnson Omojojuola", "balance": 12000},
    "5583920147": {"pin": "4471", "name": "Chidinma Okafor", "balance": 8500},
    "9027461385": {"pin": "1122", "name": "Emeka Nwosu", "balance": 200},
    "3345678901": {"pin": "0099", "name": "Fatima Bello", "balance": 25000},
    "6612349087": {"pin": "5567", "name": "Tunde Adebayo", "balance": 0},
}

atm_vault_cash = 100000

card_number = input("Please enter your card number: ")

if card_number in bank_records:
    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        pin = input("Please enter your PIN: ")

        if pin == bank_records[card_number]["pin"]:
            name = bank_records[card_number]["name"]
            print(f"Welcome, {name}! Login successful.")

            # Menu loop — only runs after successful login
            while True:
                print("\n--- ATM Menu ---")
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Transfer Funds")
                print("5. Change PIN")
                print("6. Exit")
                choice = input("Choose an option (1-6): ")

                if choice == "1":
                    balance = bank_records[card_number]["balance"]
                    print(f"Your current balance is ₦{balance}")

                elif choice == "2":
                    amount = float(input("Enter amount to deposit: ₦"))
                    if amount <= 0:
                        print("Invalid amount. Deposit must be greater than zero.")
                    else:
                        bank_records[card_number]["balance"] += amount
                        atm_vault_cash += amount
                        print(
                            f"Deposit successful! New balance: ₦{bank_records[card_number]['balance']}")

                elif choice == "3":
                    amount = float(input("Enter amount to withdraw: ₦"))
                    if amount <= 0:
                        print("Invalid amount. Withdrawal must be greater than zero.")
                    elif amount > bank_records[card_number]["balance"]:
                        print("Insufficient funds in your account.")
                    elif amount > atm_vault_cash:
                        print(
                            "ATM is unable to dispense this amount. Please try a smaller amount.")
                    else:
                        bank_records[card_number]["balance"] -= amount
                        atm_vault_cash -= amount
                        print(
                            f"Withdrawal successful! New balance: ₦{bank_records[card_number]['balance']}")

                elif choice == "4":
                    recipient_card = input("Enter recipient's card number: ")
                    if recipient_card not in bank_records:
                        print("Recipient account not found.")
                    elif recipient_card == card_number:
                        print("You cannot transfer to your own account.")
                    else:
                        amount = float(input("Enter amount to transfer: ₦"))
                    if amount <= 0:
                        print("Invalid amount. Transfer must be greater than zero.")
                    elif amount > bank_records[card_number]["balance"]:
                        print("Insufficient funds in your account.")
                    else:
                        bank_records[card_number]["balance"] -= amount
                        bank_records[recipient_card]["balance"] += amount
                        recipient_name = bank_records[recipient_card]["name"]
                        print(
                            f"Transfer successful! ₦{amount} sent to {recipient_name}. New balance: ₦{bank_records[card_number]['balance']}")

                elif choice == "5":
                    current_pin = input("Enter your current PIN: ")
                    if current_pin != bank_records[card_number]["pin"]:
                        print("Incorrect current PIN.")
                    else:
                        new_pin = input("Enter new PIN: ")
                        confirm_pin = input("Confirm new PIN: ")
                    if new_pin != confirm_pin:
                        print("PINs do not match. PIN not changed.")
                    else:
                        bank_records[card_number]["pin"] = new_pin
                        print("PIN changed successfully!")

                elif choice == "6":
                    print("Thank you for banking with us. Goodbye!")
                    break

                else:
                    print("Invalid option, please try again.")

            break  # exits the PIN attempt loop once logged in and menu is done

        else:
            attempts += 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print(f"Incorrect PIN. You have {remaining} attempt(s) left.")
            else:
                print("Too many incorrect attempts. Card locked.")
else:
    print("Card number not recognized.")
