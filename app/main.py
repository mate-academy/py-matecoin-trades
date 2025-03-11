import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades_list = json.load(file)
    matecoin_account = 0
    earned_money = 0

    for trade in trades_list:
        if trade["bought"] is not None:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= (Decimal(trade["matecoin_price"])
                             * Decimal(trade["bought"]))
        if trade["sold"] is not None:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += (Decimal(trade["matecoin_price"])
                             * Decimal(trade["sold"]))

    profit_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_dict, file)
