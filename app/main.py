import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with (open(file_name, "r") as trades_json,
          open("profit.json", "w") as profit_json):
        trades = json.load(trades_json)
        earned_money = Decimal("0")
        matecoin_account = Decimal("0")
        for trade in trades:
            matecoin_price = Decimal(trade["matecoin_price"])
            if trade["bought"]:
                bought = Decimal(trade["bought"])
                earned_money -= bought * matecoin_price
                matecoin_account += bought
            if trade["sold"]:
                sold = Decimal(trade["sold"])
                earned_money += sold * matecoin_price
                matecoin_account -= sold
        json.dump({
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }, profit_json, indent=2)
