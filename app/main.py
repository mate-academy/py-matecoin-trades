import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades_data = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_data:
        bought = Decimal(trade.get("bought") or "0")
        sold = Decimal(trade.get("sold") or "0")
        matecoin_price = Decimal(trade.get("matecoin_price"))

        matecoin_account += bought - sold
        earned_money -= bought * matecoin_price
        earned_money += sold * matecoin_price

    income_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(income_data, file, indent=2)
