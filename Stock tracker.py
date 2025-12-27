# Welcome message
print("---------------------------------\n")
print("   Welcome to the Stock Tracker!   ")
print("---------------------------------\n")

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330
}

total_investment = 0
portfolio = []

print("Available stocks:")
for stock in stock_prices:
    print(f"- {stock}")

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("❌ Stock not found. Please choose from the list.")
        continue
    try:
        quantity = int(input(f"Enter quantity of {stock}: "))
        if quantity <= 0:
            print("❌ Quantity must be greater than zero.")
            continue
    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    price = stock_prices[stock]
    value = price * quantity

    portfolio.append((stock, quantity, price, value))
    total_investment += value

    print(f"✅ Added {quantity} shares of {stock}")

print("\n--------- Investment Summary ---------")
for stock, qty, price, value in portfolio:
    print(f"{stock}: {qty} * ${price} = ${value}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Optional file saving
save = input("\nWould you like to save this to a file? (yes/no): ").lower()

if save == "yes":
    with open("portfolio.txt", "w") as file:
        file.write("Stock | Quantity | Price | Value\n")
        file.write("-----------------------------------\n")
        for stock, qty, price, value in portfolio:
            file.write(f"{stock} | {qty} | {price} | {value}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}")

    print("📁 Portfolio saved to portfolio.txt")

# Thank you message
print("\n---------------------------------")
print(" Thank you for using Stock Tracker ")
print("---------------------------------")