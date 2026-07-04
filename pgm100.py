from datetime import datetime

# Invoice details
customer_name = input("Enter Customer Name: ")

num_items = int(input("How many products? "))

invoice = []
grand_total = 0

for i in range(num_items):
    print(f"\nProduct {i+1}")

    product = input("Product Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per Unit: "))

    total = quantity * price
    grand_total += total

    invoice.append([product, quantity, price, total])

# Invoice Content
invoice_text = "\n"
invoice_text += "=" * 50 + "\n"
invoice_text += "            INVOICE BILL\n"
invoice_text += "=" * 50 + "\n"
invoice_text += f"Customer Name : {customer_name}\n"
invoice_text += f"Date          : {datetime.now()}\n"
invoice_text += "-" * 50 + "\n"
invoice_text += "{:<20} {:<10} {:<10} {:<10}\n".format(
    "Product", "Qty", "Price", "Total"
)
invoice_text += "-" * 50 + "\n"

print("invoice",invoice)
for item in invoice:
    invoice_text += "{:<20} {:<10} {:<10} {:<10}\n".format(
        item[0], item[1], item[2], item[3]
    )

invoice_text += "-" * 50 + "\n"
invoice_text += f"Grand Total : Rs.{grand_total}\n"
invoice_text += "=" * 50 + "\n"

# Display Invoice
print(invoice_text)

# Save Invoice
filename = f"invoice_{customer_name}.txt"

with open(filename, "w") as file:
    file.write(invoice_text)

print(f"Invoice saved successfully as {filename}")