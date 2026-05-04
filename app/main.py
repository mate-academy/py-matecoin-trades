import json
from decimal import Decimal
from typing import Any


def from_json_to_dict(file_path: str) -> Any:
    with open(file_path, "r") as file:
        data = json.load(file)
    return data


def from_dict_to_json(file_path: str, data: Any) -> None:
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def calculate_profit(file_path: str) -> None:
    trades = from_json_to_dict(file_path)

    balance_usd = Decimal("0")
    balance_coin = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade.get("bought") is not None:
            bought = Decimal(trade["bought"])
            balance_usd -= bought * price
            balance_coin += bought

        if trade.get("sold") is not None:
            sold = Decimal(trade["sold"])
            balance_usd += sold * price
            balance_coin -= sold

    result = {
        "earned_money": str(balance_usd),
        "matecoin_account": str(balance_coin)
    }
    from_dict_to_json("profit.json", result)
