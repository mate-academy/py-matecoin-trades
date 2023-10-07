import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        trades = json.load(file)
        earned_money = Decimal(0)
        matecoin_account = Decimal(0)
        for action in trades:
            if action.get("bought"):
                matecoin_account += Decimal(action.get("bought"))
                earned_money -= (Decimal(action.get("bought"))
                                 * Decimal(action.get("matecoin_price")))

            if action.get("sold"):
                matecoin_account -= Decimal(action.get("sold"))
                earned_money += (Decimal(action.get("sold"))
                                 * Decimal(action.get("matecoin_price")))
        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        with open("profit.json", "w") as profit:
            json.dump(result, profit, indent=2)
