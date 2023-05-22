import json
from decimal import Decimal


path_to_file = "/Users/admin/py-matecoin-trades/app/trades.json"


def calculate_profit(path_to_file: str) -> None:
    with open(path_to_file) as f:
        user_profit = json.load(f)
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)
    for i in user_profit:
        if i["sold"] is not None:
            earned_money += Decimal(i["sold"]) * Decimal(i["matecoin_price"])
            matecoin_account -= Decimal(i["sold"])
        if i["bought"] is not None:
            earned_money -= Decimal(i["bought"]) * Decimal(i["matecoin_price"])
            matecoin_account += Decimal(i["bought"])
    profit = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
