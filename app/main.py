import json
from decimal import Decimal


def calculate_profit(file_name: str, output_file: str = "profit.json") -> None:
    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")
    with open(file_name, "r") as f:
        trades = json.load(f)
    for trade in trades:
        bought = Decimal(trade["bought"]) if trade["bought"] \
            else Decimal("0.0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0.0")
        matecoin_price = Decimal(trade["matecoin_price"])

        matecoin_account += bought
        earned_money -= bought * matecoin_price
        matecoin_account -= sold
        earned_money += sold * matecoin_price

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open(output_file, "w") as f:
        json.dump(profit_data, f, indent=4)


calculate_profit("trades.json")
