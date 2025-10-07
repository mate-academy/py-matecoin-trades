import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    # Load trades from JSON file
    with open(filename, "r") as f:
        trades = json.load(f)

    # Initialize variables using Decimal for precision
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    # Process each trade
    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            # Buying coins - subtract money, add coins
            bought_volume = Decimal(trade["bought"])
            money_spent = bought_volume * matecoin_price
            earned_money -= money_spent
            matecoin_account += bought_volume

        if trade["sold"] is not None:
            # Selling coins - add money, subtract coins
            sold_volume = Decimal(trade["sold"])
            money_received = sold_volume * matecoin_price
            earned_money += money_received
            matecoin_account -= sold_volume

    # Prepare result dictionary with string values
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    # Save result to profit.json
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)


# Execute the function
if __name__ == "__main__":
    calculate_profit("trades.json")
