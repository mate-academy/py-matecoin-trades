import json
from decimal import Decimal


def calculate_profit(filename: json) -> None:
    # Load trades data from JSON file
    with open(filename, "r") as f:
        trades = json.load(f)

    # Initialize variables
    total_profit = Decimal(0)  # Total profit in dollars
    matecoin_balance = Decimal(0)  # Current Matecoin balance

    # Process each trade
    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        price = Decimal(trade["matecoin_price"])  # Convert price to De

        if bought:
            bought_amount = Decimal(bought)  # Convert bought amount to
            matecoin_balance += bought_amount
            total_profit -= bought_amount * price  # Subtract money
        if sold:
            sold_amount = Decimal(sold)  # Convert sold amou
            matecoin_balance -= sold_amount
            total_profit += sold_amount * price  # Add money ea

    # Prepare the result dictionary with string values
    result = {
        "earned_money": str(total_profit),  # Convert to string
        "matecoin_account": str(matecoin_balance)  # Convert to string
    }

    # Write result to profit.json
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
