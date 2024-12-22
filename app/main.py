import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit_dict = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    with open(file_name, "r") as file:
        trades = json.load(file)

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        bought = Decimal(trade["bought"]) if trade["bought"] is not None else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] is not None else Decimal("0")

        profit_dict["earned_money"] += (sold - bought) * price
        profit_dict["matecoin_account"] += bought - sold

    profit_dict["earned_money"] = str(profit_dict["earned_money"])
    profit_dict["matecoin_account"] = str(profit_dict["matecoin_account"])
    with open("profit.json", "w") as file:
        json.dump(profit_dict, file, indent=2)
