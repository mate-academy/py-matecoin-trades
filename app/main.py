import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    with open(name_file, "r") as file:
        trade_date = json.load(file)
        profit = 0
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)
    for trade in trade_date:
        if trade["bought"] is not None:
            bouhgt_volume = Decimal(trade["bought"])
            matecoin_account += bouhgt_volume
            earned_money -= bouhgt_volume * Decimal(trade["matecoin_price"])
        if trade["sold"] is not None:
            sold_volume = Decimal(trade["sold"])
            matecoin_account -= sold_volume
            earned_money += sold_volume * Decimal(trade["matecoin_price"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("../profit.json", "w") as file:
        json.dump(profit, file, indent=2)
