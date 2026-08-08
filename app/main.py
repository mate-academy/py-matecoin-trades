import json
from decimal import Decimal


def calculate_profit(trades_information: json) -> None:
    with open(trades_information) as f:
        trades = json.load(f)

    profit = {"earned_money": Decimal("0"), "matecoin_account": Decimal("0")}

    for trade in trades:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        price = Decimal(trade["matecoin_price"])

        profit["matecoin_account"] += bought - sold
        profit["earned_money"] += sold * price - bought * price

    profit = {key: str(value) for key, value in profit.items()}

    with open("profit.json", "w") as new_file:
        json.dump(profit, new_file, indent=2)
