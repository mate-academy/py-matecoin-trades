import json
from decimal import Decimal


def calculate_profit(info: str) -> None:
    with open(info) as f:
        open_ = json.load(f)
    earned_money = 0
    matecoin_account = 0

    for i in open_:
        if i["bought"] is not None:
            matecoin_account += Decimal(i["bought"])
            earned_money -= Decimal(i["bought"]) * Decimal(i["matecoin_price"])
        if i["sold"] is not None:
            matecoin_account -= Decimal(i["sold"])
            earned_money += Decimal(i["sold"]) * Decimal(i["matecoin_price"])
    info_for_profit = {"earned_money": str(earned_money),
                       "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as q:
        json.dump(info_for_profit, q, indent=2)
