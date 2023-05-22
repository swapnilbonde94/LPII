# Define an empty dictionary to store stock information
stocks = {}

def recommend_trading(strategy):
    # Perform recommendation based on trading strategy
    # This is a simplified example, you can expand this with more complex rules and conditions
    if strategy == "trend_following":
        return "Buy"
    elif strategy == "mean_reversion":
        return "Sell"
    else:
        return "No recommendation"

# Function to add stock information
def add_stock(stock_id, name, recommendation):
    stocks[stock_id] = {"Name": name, "recommendation": recommendation}
    print("Stock information added successfully.")

# Function to remove stock information
def remove_stock(stock_id):
    if stock_id in stocks:
        del stocks[stock_id]
        print("Stock information removed successfully.")
    else:
        print("Stock not found.")

# Function to display all stock information
def display_stocks():
    if stocks:
        print("Stock Information:")
        print("ID\t|\tName\t|\trecommendation")
        for stock_id, stock_info in stocks.items():
            print(f"{stock_id}\t|\t{stock_info['Name']}\t|\t{stock_info['recommendation']}")
    else:
        print("No stock information available.")

# Function to search for stock information
def search_stock(stock_id):
    if stock_id in stocks:
        stock_info = stocks[stock_id]
        print(f"ID\t|\tName\t|\trecommendation")
        print(f"{stock_id}\t|\t{stock_info['Name']}\t|\t{stock_info['recommendation']}")
    else:
        print("Stock not found.")

# Main program loop
while True:
    print("\n--- Stock Market Trading Expert System ---")
    print("1. Add stock information")
    print("2. Remove stock information")
    print("3. Display stock information")
    print("4. Search stock information")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        stock_id = input("Enter stock ID: ")
        name = input("Enter stock name: ")
        strategy = input("Enter trading strategy: ")
        recommendation = recommend_trading(strategy)
        add_stock(stock_id, name, recommendation)
    elif choice == "2":
        stock_id = input("Enter stock ID to remove: ")
        remove_stock(stock_id)
    elif choice == "3":
        display_stocks()
    elif choice == "4":
        stock_id = input("Enter stock ID to search: ")
        search_stock(stock_id)
    elif choice == "5":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
