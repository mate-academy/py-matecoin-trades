import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        trades = json.load(json_file)
        earned_money = Decimal("0")
        matecoin_account = Decimal("0")
        for trade in trades:
            bought = Decimal(trade.get("bought", "0") or "0")
            sold = Decimal(trade.get("sold", "0") or "0")
            matecoin_price = Decimal(trade["matecoin_price"])
            if bought:
                earned_money -= bought * matecoin_price
                matecoin_account += bought
            if sold > Decimal("0"):
                earned_money += sold * matecoin_price
                matecoin_account -= sold
        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
