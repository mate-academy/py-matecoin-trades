import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trades:
        if trade["bought"] is not None:
            bought_price = Decimal(
                trade.get("bought")) * Decimal(trade.get("matecoin_price"))
            matecoin_account += Decimal(trade.get("bought"))
            earned_money -= bought_price
        if trade["sold"] is not None:
            income = Decimal(
                trade.get("sold")) * Decimal(trade.get("matecoin_price"))
            matecoin_account -= Decimal(trade.get("sold"))
            earned_money += income

    result_dict = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)
                   }

    with open("profit.json", "w") as file:
        json.dump(result_dict, file, indent=2)
