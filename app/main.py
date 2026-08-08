import json
from decimal import Decimal


def calculate_profit(json_name: str) -> None:
    with open(json_name, "r") as f:
        new = json.load(f)
    total_bought = Decimal("0.0")
    total_sold = Decimal("0.0")
    total_earn = Decimal("0.0")
    total_spend = Decimal("0.0")
    for dic in new:
        if dic["bought"] is not None:
            total_bought += Decimal(dic["bought"])
            total_spend += (Decimal(dic["bought"])
                            * Decimal(dic["matecoin_price"]))

        if dic["sold"] is not None:
            total_sold += Decimal(dic["sold"])
            total_earn += Decimal(dic["sold"]) * Decimal(dic["matecoin_price"])
    earned_money = total_earn - total_spend
    matecoin_account = total_bought - total_sold
    dict_coin = {
        "earned_money" : str(earned_money),
        "matecoin_account" : str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(dict_coin, f, indent=2)
