import os

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_price(self):
        return self.price * self.quantity

class Receipt:
    def __init__(self, tax_rate=0.1, discount_rate=0.05, discount_threshold=100):
        self.items = []
        self.tax_rate = tax_rate
        self.discount_rate = discount_rate
        self.discount_threshold = discount_threshold

    def add_item(self, item):
        self.items.append(item)
    
    def calculate_subtotal(self):
        return sum(item.total_price() for item in self.items)
    
    def calculate_tax(self, subtotal):
        return subtotal * self.tax_rate
    
    def calculate_discount(self, subtotal):
        if subtotal > self.discount_threshold:
            return subtotal * self.discount_rate
        return 0
    
    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(subtotal)
        discount = self.calculate_discount(subtotal)
        return subtotal + tax - discount

    def generate_receipt(self):
        receipt_lines = []
        receipt_lines.append("Itemized Receipt\n")
        receipt_lines.append(f"{'Item':<20}{'Price':<10}{'Quantity':<10}{'Total'}\n")
        receipt_lines.append("-" * 50 + "\n")
        
        for item in self.items:
            receipt_lines.append(f"{item.name:<20}{item.price:<10}{item.quantity:<10}{item.total_price()}\n")
        
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax(subtotal)
        discount = self.calculate_discount(subtotal)
        total = self.calculate_total()

        receipt_lines.append("\n")
        receipt_lines.append(f"{'Subtotal:':<40}{subtotal:.2f}\n")
        receipt_lines.append(f"{'Tax (10%):':<40}{tax:.2f}\n")
        if discount > 0:
            receipt_lines.append(f"{'Discount (5%):':<40}{-discount:.2f}\n")
        receipt_lines.append(f"{'Total:':<40}{total:.2f}\n")

        return receipt_lines
    
    def save_receipt(self, filename="receipt.txt"):
        receipt_data = self.generate_receipt()
        with open(filename, 'w') as f:
            f.writelines(receipt_data)
        print(f"Receipt saved to {filename}")

# Main program
if __name__ == "__main__":
    receipt = Receipt()

    while True:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == 'done':
            break
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))

        item = Item(name, price, quantity)
        receipt.add_item(item)

    receipt_lines = receipt.generate_receipt()
    for line in receipt_lines:
        print(line, end='')

    save_choice = input("Do you want to save the receipt to a file? (yes/no): ").lower()
    if save_choice == 'yes':
        receipt.save_receipt()
