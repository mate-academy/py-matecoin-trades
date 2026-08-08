import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(filename) as file:
        trades = json.load(file)
    for trade in trades:
        if trade.get("bought"):
            matecoin_account += Decimal(trade.get("bought"))
            earned_money -= Decimal(trade.get("bought")) * \
                Decimal(trade.get("matecoin_price"))
        if trade.get("sold"):
            matecoin_account -= Decimal(trade.get("sold"))
            earned_money += Decimal(trade.get("sold")) *\
                Decimal(trade.get("matecoin_price"))
    with open("profit.json", "w") as report:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            report,
            indent=2
        )
