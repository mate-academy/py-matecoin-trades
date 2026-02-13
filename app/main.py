# flake8: noqa: *
import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")
    with open(file_name) as json_file:
        data = json.load(json_file)
        for trade in data:
            if trade.get("bought") is not None:
                earned_money -= Decimal(trade.get("bought")) * Decimal(trade.get("matecoin_price"))
                matecoin_account += Decimal(trade.get("bought"))
            if trade.get("sold") is not None:
                earned_money += Decimal(trade.get("sold")) * Decimal(trade.get("matecoin_price"))
                matecoin_account -= Decimal(trade.get("sold"))
    with open("profit.json", "w") as json_file:
        json.dump({
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account),
            }, json_file, indent=2)

