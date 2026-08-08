import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    res = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    with open(file_name) as file:
        trades = json.load(file)

    for trade in trades:
        bought, sold, matecoin_price = trade.values()

        if bought:
            res["earned_money"] -= Decimal(bought) * Decimal(matecoin_price)
            res["matecoin_account"] += Decimal(bought)

        if sold:
            res["earned_money"] += Decimal(sold) * Decimal(matecoin_price)
            res["matecoin_account"] -= Decimal(sold)

    with open("profit.json", "w") as file:
        json.dump({key: str(val) for key, val in res.items()}, file, indent=2)
