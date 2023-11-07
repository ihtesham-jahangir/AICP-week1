# Define the price for each component in a dictionary
component_prices = {
    'A1': 75.00,
    'A2': 150.00,
    'B1': 79.99,
    'B2': 149.99,
    'B3': 299.99,
    'C1': 49.99,
    'C2': 89.99,
    'C3': 129.99,
    'D1': 59.99,
    'D2': 119.99,
    'E1': 49.99,
    'E2': 89.99,
    'E3': 129.99,
    'F1': 50.00,
    'F2': 100.00,
    'G1': 100.00,
    'G2': 175.00
}

# Define the basic set of components
basic_components = ['A1', 'B1', 'C1']

# Initialize the total cost with the basic set of components
total_cost = 200.00
chosen_items = basic_components.copy()

def validate_input(prompt, valid_choices):
    while True:
        choice = input(prompt)
        if choice in valid_choices:
            return choice
        else:
            print("Invalid choice. Please enter a valid item code.")

# Task 1: Choosing one case, one RAM, and one Main Hard Disk Drive
print("Task 1: Choosing one case, one RAM, and one Main Hard Disk Drive")

print("Category: Case")
selected_case = validate_input("Enter the item code (A1/A2): ", ['A1', 'A2'])
chosen_items.append(selected_case)
total_cost += component_prices[selected_case]

print("\nCategory: RAM")
selected_ram = validate_input("Enter the item code (B1/B2/B3): ", ['B1', 'B2', 'B3'])
chosen_items.append(selected_ram)
total_cost += component_prices[selected_ram]

print("\nCategory: Main Hard Disk Drive")
selected_hdd = validate_input("Enter the item code (C1/C2/C3): ", ['C1', 'C2', 'C3'])
chosen_items.append(selected_hdd)
total_cost += component_prices[selected_hdd]

# Display the chosen items and the price of the computer
print("\nChosen items:")
for item_code in chosen_items:
    print(f"{item_code} - {component_prices[item_code]:.2f} USD")

print(f"Total cost of the computer: {total_cost:.2f} USD")

# Task 2: Ordering additional items
print("\nTask 2: Ordering additional items")

while True:
    print("Do you want to purchase additional items?")
    additional_choice = input("Enter 'yes' or 'no': ").lower()
    if additional_choice != 'yes':
        break

    print("\nCategory: Solid State Drive")
    print("D1 - 240 GB SSD ($59.99)")
    print("D2 - 480 GB SSD ($119.99)")

    selected_ssd = validate_input("Enter the item code (D1/D2) or press Enter to skip: ", ['D1', 'D2'])
    if selected_ssd:
        chosen_items.append(selected_ssd)
        total_cost += component_prices[selected_ssd]

    print("\nCategory: Second Hard Disk Drive")
    print("E1 - 1 TB HDD ($49.99)")
    print("E2 - 2 TB HDD ($89.99)")
    print("E3 - 4 TB HDD ($129.99)")

    selected_second_hdd = validate_input("Enter the item code (E1/E2/E3) or press Enter to skip: ", ['E1', 'E2', 'E3'])
    if selected_second_hdd:
        chosen_items.append(selected_second_hdd)
        total_cost += component_prices[selected_second_hdd]

    print("\nCategory: Optical Drive")
    print("F1 - DVD/Blu-Ray Player ($50.00)")
    print("F2 - DVD/Blu-Ray Re-writer ($100.00)")

    selected_optical_drive = validate_input("Enter the item code (F1/F2) or press Enter to skip: ", ['F1', 'F2'])
    if selected_optical_drive:
        chosen_items.append(selected_optical_drive)
        total_cost += component_prices[selected_optical_drive]

# Task 3: Offering discounts
print("\nTask 3: Offering discounts")

additional_items_count = len(chosen_items) - 3  # Subtracting the basic items
discounted_cost = total_cost

if additional_items_count == 1:
    discount_percentage = 5
    discounted_cost = total_cost * (1 - discount_percentage / 100)
elif additional_items_count >= 2:
    discount_percentage = 10
    discounted_cost = total_cost * (1 - discount_percentage / 100)

money_saved = total_cost - discounted_cost

print(f"Amount of money saved: {money_saved:.2f} USD")
print(f"New price of the computer after discount: {discounted_cost:.2f} USD")
