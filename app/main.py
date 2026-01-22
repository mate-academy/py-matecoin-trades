import json
from decimal import Decimal
from typing import Dict


def calculate_profit(file_name: str) -> None:
    # Initialize variables
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    # Load trades from file
    with open(file_name, "r") as f:
        trades = json.load(f)

    # Process each trade
    for trade in trades:
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            matecoin_account += bought
            earned_money -= bought * price
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            matecoin_account -= sold
            earned_money += sold * price

    # Prepare data to write to file
    data: Dict[str, str] = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    # Write data to file
    with open("profit.json", "w") as f:
        json.dump(data, f, indent=2)
