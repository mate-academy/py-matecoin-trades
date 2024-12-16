import json
from decimal import Decimal


def calculate_profit(trade_list: str = "trades.json") -> None:
    sum_bought = 0
    multy_bought = 0
    sum_sold = 0
    multy_sold = 0
    with open(trade_list, "r") as data:
        calculate = json.load(data)

    for i in calculate:
        if i["bought"]:
            sum_bought += Decimal(i["bought"])
            multy_bought += Decimal(i["bought"]) * Decimal(i["matecoin_price"])
        if i["sold"]:
            sum_sold += Decimal(i["sold"])
            multy_sold += Decimal(i["sold"]) * Decimal(i["matecoin_price"])
    account = Decimal(sum_bought) - Decimal(sum_sold)
    money = Decimal(multy_sold) - Decimal(multy_bought)
    with open("profit.json", "w") as profit:
        json.dump({"earned_money": f"{money}",
                   "matecoin_account": f"{account}"}, profit, indent=2)
