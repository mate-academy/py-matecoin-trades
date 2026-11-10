import json
from decimal import Decimal


def calculate_profit(trades_file_path: str) -> None:
    with open(trades_file_path, "r") as file_in:
        trades = json.load(file_in)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(str(trade["matecoin_price"]))

        if trade.get("bought") is not None:
            bought_amount = Decimal(str(trade["bought"]))
            matecoin_account += bought_amount
            earned_money -= bought_amount * price

        if trade.get("sold") is not None:
            sold_amount = Decimal(str(trade["sold"]))
            matecoin_account -= sold_amount
            earned_money += sold_amount * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file_out:
        json.dump(result, file_out, indent=2)
