import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    earned_money = Decimal("0")  # Tracks total earned money
    matecoin_account = Decimal("0")  # Tracks the number of Matecoins owned

    # Read the trades data from the JSON file
    with open(filename, "r") as file:
        trades = json.load(file)

    # Process each trade
    for trade in trades:
        if trade["bought"] is not None:
            # If bought, subtract the money and add Matecoins
            bought_amount = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            earned_money -= bought_amount * price
            matecoin_account += bought_amount
        if trade["sold"] is not None:
            # If sold, add the money and subtract Matecoins
            sold_amount = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            earned_money += sold_amount * price
            matecoin_account -= sold_amount

    # Prepare the result for writing to profit.json
    result = {
        "earned_money": str(earned_money),  # Store as a string
        "matecoin_account": str(matecoin_account)  # Store as a string
    }

    # Write the result to profit.json
    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
