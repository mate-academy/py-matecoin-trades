import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = 0
    account = 0
    with open(file_name, "r") as date_file, \
         open("profit.json", "w") as profit_file:
        for data in json.load(date_file):
            if data.get("bought"):
                account += Decimal(data.get("bought"))
                earned_money -= Decimal(data.get("bought")) * \
                    Decimal(data.get("matecoin_price"))
            if data.get("sold"):
                account -= Decimal(data.get("sold"))
                earned_money += Decimal(data.get("sold")) * \
                    Decimal(data.get("matecoin_price"))
        res = {
            "earned_money": str(earned_money),
            "matecoin_account": str(account)
        }
        json.dump(res, profit_file, indent=2)
