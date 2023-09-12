import os
import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    sum_bought = Decimal("0")
    money_bought = Decimal("0")
    sum_sold = Decimal("0")
    money_sold = Decimal("0")

    with open(name_file) as f:
        trader_data = json.load(f)

    for elem in trader_data:
        if elem["bought"] is not None:
            sum_bought += Decimal(elem["bought"])
            money_bought += sum_bought * Decimal(elem["matecoin_price"])

        if elem["sold"] is not None:
            sum_sold += Decimal(elem["sold"])
            money_sold += sum_sold * Decimal(elem["matecoin_price"])

    balance_money = money_sold - money_bought
    balance_account = sum_bought - sum_sold

    dic = {
        "earned_money": str(balance_money),
        "matecoin_account": str(balance_account)
    }

    path_file2 = os.path.join(os.getcwd(), "profit.json")

    with open(path_file2, "w") as f2:
        json.dump(dic, f2)


path_file = os.path.join(os.getcwd(), "trades.json")

calculate_profit(path_file)
