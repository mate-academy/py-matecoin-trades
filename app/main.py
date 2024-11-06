import json
from decimal import Decimal, getcontext

# Set precision for Decimal calculations
getcontext().prec = 10


def calculate_profit(filename: str) -> None:
    # Load trades from the provided JSON file
    with open(filename, "r") as file:
        trades = json.load(file)

    # Initialize variables for tracking Matecoin balance and profit
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    # Process each trade in the trades list
    for trade in trades:
        bought = Decimal(trade["bought"]) if (trade["bought"]
                                              is not None) else Decimal("0")
        sold = Decimal(trade["sold"]) if (trade["sold"]
                                          is not None) else Decimal("0")
        price = Decimal(trade["matecoin_price"])

        # Update Matecoin account and earned money based on bought/sold values
        matecoin_account += bought
        matecoin_account -= sold
        earned_money += sold * price
        earned_money -= bought * price

    # Prepare the result dictionary
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    # Write the result to profit.json in JSON format
    with open("profit.json", "w") as outfile:
        json.dump(result, outfile, indent=2)
