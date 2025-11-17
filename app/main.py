import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    matecoin_account, earned_money = Decimal(0), Decimal(0)
    with open(filename, "r") as f:
        trades = json.load(f)  # прямо json.load без read()

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        bought = Decimal(trade["bought"]) if (
            trade.get("bought")) else Decimal(0)
        sold = Decimal(trade["sold"]) if trade.get("sold") else Decimal(0)

        matecoin_account += bought - sold
        earned_money += price * bought - price * sold

    with open("profit.json", "w") as f:
        json.dump(
            {
                "earned_money": f"{earned_money}",
                "matecoin_account": f"{matecoin_account}",
            },
            f,
            indent=2  # гарний формат
        )
