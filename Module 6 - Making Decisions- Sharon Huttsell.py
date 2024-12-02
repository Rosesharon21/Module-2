BASE_FEE = 5.00
FEE_AFTER_100 = 0.03
FEE_AFTER_300 = 0.02
TAX_RATE = 0.14
SENTINEL_VALUE = -1

customer_data_list = []

def calculate_bill(text_messages):
    if text_messages <= 100:
        bill = BASE_FEE
    elif text_messages <= 300:
        bill = BASE_FEE + (text_messages - 100) * FEE_AFTER_100
    else:
        bill = BASE_FEE + (200 * FEE_AFTER_100) + (text_messages - 300) * FEE_AFTER_300
    total_bill = bill + (bill * TAX_RATE)
    return bill, total_bill

while True:
    area_code = input("Enter area code (three digits) or -1 to quit: ")
    if area_code == str(SENTINEL_VALUE):
        break

    phone_number = input("Enter phone number (seven digits): ")
    text_messages = int(input("Enter total number of text messages sent: "))

    bill, total_bill = calculate_bill(text_messages)

    customer_data_list.append((area_code, phone_number, text_messages, bill, total_bill))

    print(f"Area Code: {area_code}")
    print(f"Phone Number: {phone_number}")
    print(f"Text Messages Sent: {text_messages}")
    print(f"Monthly Bill (before tax): ${bill:.2f}")
    print(f"Monthly Bill (after tax): ${total_bill:.2f}")

print("\nAll Customer Data: ")
for customer in customer_data_list:
    print(customer)

specific_area_code = input("\nEnter a three-digit area code to view bills from that specific area or -1 to quit: ")
if specific_area_code != str(SENTINEL_VALUE):
    print(f"\nCustomers from area code {specific_area_code}:")
    for customer in customer_data_list:
        if customer[0] == specific_area_code:
            print(customer)

print("\nCustomers with over 100 text messages: ")
for customer in customer_data_list:
    if customer[2] > 100:
        print(customer)

print("\nCustomers with total bill exceeding $10: ")
for customer in customer_data_list:
    if customer[4] > 10:
        print(customer)
