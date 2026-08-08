import json
from decimal import Decimal


def calculate_profit(file_name: str) -> json:
    earned_money = 0
    matecoin_account = 0
    with open(file_name) as f:
        trades_data = json.load(f)
        for i in trades_data:
            if i["bought"]:
                earned_money -= Decimal(i["bought"])\
                    * Decimal(i["matecoin_price"])
                matecoin_account += Decimal(i["bought"])
            if i["sold"]:
                earned_money += Decimal(i["sold"])\
                    * Decimal(i["matecoin_price"])
                matecoin_account -= Decimal(i["sold"])
    with open("profit.json", "w") as f:
        json.dump({"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}, f, indent=2)
