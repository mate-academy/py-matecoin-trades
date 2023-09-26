import json
from decimal import Decimal


def calculate_profit(trades_file) -> None:
    # Load data from trades.json
    with open(trades_file, "r") as f:
        trades_data = json.load(f)

    # Initialize variables for profit calculation
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    # Iterate through trades data
    for trade in trades_data:
        bought = trade.get("bought", None)
        sold = trade.get("sold", None)
        matecoin_price = Decimal(trade["matecoin_price"])

        if bought is not None:
            bought_amount = Decimal(bought)
            earned_money -= bought_amount * matecoin_price
            matecoin_account += bought_amount

        if sold is not None:
            sold_amount = Decimal(sold)
            earned_money += sold_amount * matecoin_price
            matecoin_account -= sold_amount

    # Create a dictionary with the profit information
    profit_info = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    # Save the profit information to profit.json
    with open("profit.json", "w") as f:
        json.dump(profit_info, f)
