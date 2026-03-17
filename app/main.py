import json
from decimal import Decimal


def calculate_profit(file_name: str = "trades.json") -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(file_name, "r") as f:
        trades = json.load(f)
        for trade in trades:
            bought = Decimal(str(trade["bought"] or "0"))
            sold = Decimal(str(trade["sold"] or "0"))
            price = Decimal(str(trade["matecoin_price"]))
            earned_money += sold * price
            earned_money -= bought * price
            matecoin_account += bought
            matecoin_account -= sold
    result_dict = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as f:
        json.dump(result_dict, f, indent=2)
