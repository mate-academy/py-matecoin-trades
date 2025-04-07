import json
from decimal import Decimal


def calculate_profit(trades: json) -> None:
    with open(trades, "r") as file:
        trades_list = json.load(file)
    result_dict = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    for trade in trades_list:
        if trade["bought"]:
            bought, price = trade["bought"], trade["matecoin_price"]
            result_dict["matecoin_account"] += Decimal(bought)
            result_dict["earned_money"] -= Decimal(bought) * Decimal(price)
        if trade["sold"]:
            sold, price = trade["sold"], trade["matecoin_price"]
            result_dict["matecoin_account"] -= Decimal(sold)
            result_dict["earned_money"] += Decimal(sold) * Decimal(price)

    with open("profit.json", "w") as file:
        result_dict = {k: str(v) for k, v in result_dict.items()}
        json.dump(result_dict, file, indent=2)
