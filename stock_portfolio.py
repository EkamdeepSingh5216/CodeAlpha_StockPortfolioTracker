import csv
import random

STOCKS = {
    "AAPL": {"name": "Apple Inc.", "price": 180.00},
    "MSFT": {"name": "Microsoft Corporation", "price": 420.00},
    "NVDA": {"name": "NVIDIA Corporation", "price": 135.00},
    "AMZN": {"name": "Amazon.com Inc.", "price": 190.00},
    "GOOGL": {"name": "Alphabet Inc.", "price": 175.00},
    "META": {"name": "Meta Platforms Inc.", "price": 590.00},
    "TSLA": {"name": "Tesla Inc.", "price": 250.00},
    "BRK.B": {"name": "Berkshire Hathaway", "price": 500.00},
    "AVGO": {"name": "Broadcom Inc.", "price": 180.00},
    "LLY": {"name": "Eli Lilly and Company", "price": 800.00},
    "JPM": {"name": "JPMorgan Chase", "price": 210.00},
    "V": {"name": "Visa Inc.", "price": 280.00},
    "WMT": {"name": "Walmart Inc.", "price": 80.00},
    "XOM": {"name": "Exxon Mobil Corporation", "price": 115.00},
    "MA": {"name": "Mastercard Inc.", "price": 490.00},
    "COST": {"name": "Costco Wholesale", "price": 900.00},
    "ORCL": {"name": "Oracle Corporation", "price": 165.00},
    "HD": {"name": "Home Depot Inc.", "price": 360.00},
    "PG": {"name": "Procter & Gamble", "price": 170.00},
    "JNJ": {"name": "Johnson & Johnson", "price": 160.00},
    "ABBV": {"name": "AbbVie Inc.", "price": 175.00},
    "BAC": {"name": "Bank of America", "price": 40.00},
    "KO": {"name": "Coca-Cola Company", "price": 65.00},
    "NFLX": {"name": "Netflix Inc.", "price": 700.00},
    "CRM": {"name": "Salesforce Inc.", "price": 270.00},
    "AMD": {"name": "Advanced Micro Devices", "price": 160.00},
    "PEP": {"name": "PepsiCo Inc.", "price": 170.00},
    "TMO": {"name": "Thermo Fisher Scientific", "price": 550.00},
    "CSCO": {"name": "Cisco Systems Inc.", "price": 50.00},
    "ACN": {"name": "Accenture plc", "price": 350.00},
    "MCD": {"name": "McDonald's Corporation", "price": 290.00},
    "ABT": {"name": "Abbott Laboratories", "price": 115.00},
    "IBM": {"name": "International Business Machines", "price": 220.00},
    "DIS": {"name": "Walt Disney Company", "price": 100.00},
    "QCOM": {"name": "Qualcomm Inc.", "price": 170.00},
    "INTU": {"name": "Intuit Inc.", "price": 650.00},
    "TXN": {"name": "Texas Instruments", "price": 200.00},
    "AMGN": {"name": "Amgen Inc.", "price": 310.00},
    "CAT": {"name": "Caterpillar Inc.", "price": 350.00},
    "GE": {"name": "GE Aerospace", "price": 180.00},
    "NOW": {"name": "ServiceNow Inc.", "price": 800.00},
    "UBER": {"name": "Uber Technologies", "price": 75.00},
    "SHOP": {"name": "Shopify Inc.", "price": 110.00},
    "SONY": {"name": "Sony Group Corporation", "price": 90.00},
    "SPOT": {"name": "Spotify Technology", "price": 350.00},
    "ADBE": {"name": "Adobe Inc.", "price": 500.00},
    "PYPL": {"name": "PayPal Holdings", "price": 65.00},
    "INTC": {"name": "Intel Corporation", "price": 35.00},
    "F": {"name": "Ford Motor Company", "price": 12.00},
    "NKE": {"name": "Nike Inc.", "price": 80.00}
}


def display_stocks():
    stock_symbols = list(STOCKS.keys())
    random.shuffle(stock_symbols)

    print("\n" + "=" * 85)
    print("                              AVAILABLE STOCKS")
    print("=" * 85)
    print(f"{'Symbol':<12}{'Company':<42}{'Price per Share':>25}")
    print("-" * 85)

    for symbol in stock_symbols:
        company = STOCKS[symbol]["name"]
        price = STOCKS[symbol]["price"]

        print(f"{symbol:<12}{company:<42}${price:>24,.2f}")

    print("=" * 85)
    print(f"Total companies available: {len(STOCKS)}")


def display_portfolio(portfolio):
    print("\n" + "=" * 95)
    print("                                  YOUR PORTFOLIO")
    print("=" * 95)

    if not portfolio:
        print("Your portfolio is currently empty.")
        print("Choose 'Add Stock' to start building your portfolio.")
        print("=" * 95)
        return 0.0

    print(
        f"{'Symbol':<10}{'Company':<35}"
        f"{'Quantity':>12}{'Price':>18}{'Total Value':>20}"
    )
    print("-" * 95)

    total_investment = 0.0

    for symbol, quantity in portfolio.items():
        company = STOCKS[symbol]["name"]
        price = STOCKS[symbol]["price"]
        investment_value = quantity * price

        total_investment += investment_value

        print(
            f"{symbol:<10}{company:<35}"
            f"{quantity:>12,}${price:>17,.2f}"
            f"${investment_value:>19,.2f}"
        )

    print("-" * 95)
    print(f"{'TOTAL INVESTMENT':<75}${total_investment:>19,.2f}")
    print("=" * 95)

    return total_investment


def get_quantity(prompt, maximum=None):
    while True:
        value = input(prompt).strip()

        try:
            quantity = int(value)

            if quantity <= 0:
                print("Please enter a quantity greater than zero.")
                continue

            if maximum is not None and quantity > maximum:
                print(f"You can remove at most {maximum} shares.")
                continue

            return quantity

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def add_stock(portfolio):
    display_stocks()

    symbol = input(
        "\nEnter the stock symbol you want to add: "
    ).strip().upper()

    if symbol not in STOCKS:
        print("Stock symbol not found. Please select from the list.")
        return

    company = STOCKS[symbol]["name"]
    price = STOCKS[symbol]["price"]

    print(f"\nSelected company: {company}")
    print(f"Price per share: ${price:,.2f}")

    quantity = get_quantity("Enter the number of shares: ")

    portfolio[symbol] = portfolio.get(symbol, 0) + quantity

    print(f"\n{quantity} shares of {company} added successfully.")

    display_portfolio(portfolio)


def remove_stock(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty. There are no stocks to remove.")
        return

    display_portfolio(portfolio)

    symbol = input(
        "\nEnter the symbol of the stock to remove: "
    ).strip().upper()

    if symbol not in portfolio:
        print("This stock is not present in your portfolio.")
        return

    print(f"\nShares currently held: {portfolio[symbol]}")

    quantity = get_quantity(
        "Enter the number of shares to remove: ",
        maximum=portfolio[symbol]
    )

    portfolio[symbol] -= quantity

    if portfolio[symbol] == 0:
        del portfolio[symbol]

    print(f"\n{quantity} shares of {symbol} removed successfully.")

    display_portfolio(portfolio)


def save_portfolio(portfolio):
    if not portfolio:
        print("\nYour portfolio is empty. Nothing to save.")
        return

    filename = input(
        "\nEnter the CSV filename (press Enter for portfolio.csv): "
    ).strip()

    if not filename:
        filename = "portfolio.csv"

    if not filename.lower().endswith(".csv"):
        filename += ".csv"

    total_investment = sum(
        STOCKS[symbol]["price"] * quantity
        for symbol, quantity in portfolio.items()
    )

    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            writer.writerow([
                "Stock Symbol",
                "Company Name",
                "Quantity",
                "Price Per Share",
                "Investment Value"
            ])

            for symbol, quantity in portfolio.items():
                company = STOCKS[symbol]["name"]
                price = STOCKS[symbol]["price"]
                value = price * quantity

                writer.writerow([
                    symbol,
                    company,
                    quantity,
                    f"{price:.2f}",
                    f"{value:.2f}"
                ])

            writer.writerow([])
            writer.writerow(["Total Investment", "", "", "", f"{total_investment:.2f}"])

        print(f"\nPortfolio saved successfully to '{filename}'.")

    except OSError as error:
        print(f"\nUnable to save the portfolio: {error}")


def main():
    portfolio = {}

    print("\n" + "=" * 55)
    print("             STOCK PORTFOLIO TRACKER")
    print("=" * 55)
    print("Explore 50 companies and build your own portfolio.")

    while True:
        print("\nMAIN MENU")
        print("-" * 35)
        print("1. View Available Stocks")
        print("2. Add Stock to Portfolio")
        print("3. View My Portfolio")
        print("4. Remove Shares")
        print("5. Save Portfolio to CSV")
        print("6. Exit")
        print("-" * 35)

        choice = input("Select an option (1-6): ").strip()

        if choice == "1":
            display_stocks()

        elif choice == "2":
            add_stock(portfolio)

        elif choice == "3":
            display_portfolio(portfolio)

        elif choice == "4":
            remove_stock(portfolio)

        elif choice == "5":
            save_portfolio(portfolio)

        elif choice == "6":
            print("\nFinal Portfolio Summary:")
            display_portfolio(portfolio)
            print("\nThank you for using Stock Portfolio Tracker!")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()