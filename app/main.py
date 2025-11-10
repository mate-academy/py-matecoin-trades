import json
from decimal import Decimal


def calculate_profit(trades_json: str) -> None:
    profit_json = "profit.json"
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(trades_json, "r") as trades_file:
        for trade in json.load(trades_file):
            price = Decimal(trade.get("matecoin_price", "0"))

            if bought := trade.get("bought"):
                bought = Decimal(bought)
                earned_money -= bought * price
                matecoin_account += bought

            if sold := trade.get("sold"):
                sold = Decimal(sold)
                earned_money += sold * price
                matecoin_account -= sold

    with open(profit_json, "w") as profit_file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            profit_file,
            indent=2,
        )
