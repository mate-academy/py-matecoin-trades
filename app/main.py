import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    with open(name, "r") as jf:
        data_of_bit = json.load(jf)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for data in data_of_bit:
        if data["bought"] is not None:
            bought = Decimal(data["bought"])
            matecoin_price = Decimal(data["matecoin_price"])
            earned_money -= bought * matecoin_price
            matecoin_account += Decimal(data["bought"])
        if data["sold"] is not None:
            sold = Decimal(data["sold"])
            matecoin_price = Decimal(data["matecoin_price"])
            earned_money += sold * matecoin_price
            matecoin_account -= Decimal(data["sold"])

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit_data, f, indent=2)
