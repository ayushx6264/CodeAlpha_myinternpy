def stock_portfolio_tracker():
    # Hardcoded stock prices (in USD)
    stock_prices = {
        "AAPL": 190.15,   # Apple
        "MSFT": 420.72,   # Microsoft
        "GOOGL": 175.50,  # Alphabet (Google)
        "AMZN": 185.19,   # Amazon
        "TSLA": 175.34    # Tesla
    }
    
    portfolio = {}
    total_value = 0.0
    
    print("Stock Portfolio Tracker")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    
    while True:
        print("\n1. Add stock to portfolio")
        print("2. View portfolio and total value")
        print("3. Save to file and exit")
        choice = input("Enter your choice (1-3): ")
        
        if choice == "1":
            stock = input("Enter stock symbol: ").upper()
            if stock not in stock_prices:
                print("Invalid stock symbol. Available stocks:", ", ".join(stock_prices.keys()))
                continue
                
            try:
                quantity = int(input(f"Enter quantity of {stock}: "))
                if quantity <= 0:
                    print("Quantity must be positive.")
                    continue
                    
                portfolio[stock] = portfolio.get(stock, 0) + quantity
                print(f"Added {quantity} shares of {stock} to your portfolio.")
                
            except ValueError:
                print("Please enter a valid number for quantity.")
                
        elif choice == "2":
            if not portfolio:
                print("Your portfolio is empty.")
                continue
                
            print("\nYour Portfolio:")
            total_value = 0
            for stock, quantity in portfolio.items():
                value = quantity * stock_prices[stock]
                total_value += value
                print(f"{stock}: {quantity} shares @ ${stock_prices[stock]:.2f} = ${value:.2f}")
                
            print(f"\nTotal Portfolio Value: ${total_value:.2f}")
            
        elif choice == "3":
            if portfolio:
                with open("portfolio_summary.txt", "w") as f:
                    f.write("Portfolio Summary:\n")
                    for stock, quantity in portfolio.items():
                        value = quantity * stock_prices[stock]
                        f.write(f"{stock}: {quantity} shares @ ${stock_prices[stock]:.2f} = ${value:.2f}\n")
                    f.write(f"\nTotal Portfolio Value: ${total_value:.2f}")
                print("Portfolio saved to 'portfolio_summary.txt'")
            print("Exiting program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

# Start the tracker
stock_portfolio_tracker()