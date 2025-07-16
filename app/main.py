import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    operations_dict = {
        "earned_money": 0,
        "matecoin_account": 0
    }
    with open(filename, "r") as file:
        trades = json.load(file)

        for trade in trades:
            for key, value in trade.items():
                try:
                    value, price = (
                        Decimal(value),
                        Decimal(trade["matecoin_price"])
                    )
                except TypeError:
                    continue
                if key == "bought":
                    operations_dict["earned_money"] -= price * value
                    operations_dict["matecoin_account"] += value
                elif key == "sold":
                    operations_dict["earned_money"] += price * value
                    operations_dict["matecoin_account"] -= value

    profit = {key : str(value) for key, value in operations_dict.items()}
    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
