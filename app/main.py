import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    # Read trades data from JSON file
    with open(file_name, "r") as file:
        trades = json.load(file)

    total_money_spent = Decimal("0")
    total_money_earned = Decimal("0")
    matecoin_balance = Decimal("0")

    # Process each trade
    for trade in trades:
        if trade["bought"] is not None:
            bought_volume = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            total_money_spent += bought_volume * price
            matecoin_balance += bought_volume
        if trade["sold"] is not None:
            sold_volume = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            total_money_earned += sold_volume * price
            matecoin_balance -= sold_volume

    # Calculate earned money
    earned_money = total_money_earned - total_money_spent

    # Prepare result dictionary
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_balance)
    }

    # Write result to profit.json
    with open("profit.json", "w") as outfile:
        json.dump(result, outfile, indent=2)
