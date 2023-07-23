import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        data = json.load(json_file)
    earned_money = 0
    matecoin_account = 0
    for transaction in data:
        if transaction.get("bought"):
            matecoin_account += Decimal(transaction.get("bought"))
            earned_money -= (Decimal(transaction.get("bought"))
                             * Decimal(transaction.get("matecoin_price")))
        if transaction.get("sold"):
            matecoin_account -= Decimal(transaction.get("sold"))
            earned_money += (Decimal(transaction.get("sold"))
                             * Decimal(transaction.get("matecoin_price")))
    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as profit_json:
        json.dump(profit, profit_json, indent=2)