import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as trades_file:
        trades = json.load(trades_file)

    earned_money = 0
    matecoin_account = 0
    for trade in trades:
        matecoin_price = trade.get("matecoin_price", "0")
        bought = trade.get("bought", "0")\
            if trade.get("bought", "0") is not None else "0"
        sold = trade.get("sold", "0")\
            if trade.get("sold", "0") is not None else "0"
        matecoin_account += Decimal(bought) - Decimal(sold)
        earned_money += (
            Decimal(matecoin_price) * (Decimal(sold) - Decimal(bought)))

    with open("profit.json", "w") as profit_file:
        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        json.dump(profit, profit_file, indent=2)
