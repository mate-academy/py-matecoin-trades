import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        data_list = json.load(file)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for i in range(len(data_list)):
        buy, sell, prices = data_list[i].values()
        if buy:
            current = Decimal(buy) * Decimal(prices)
            earned_money -= current
            matecoin_account += Decimal(buy)
        if sell:
            current = Decimal(sell) * Decimal(prices)
            earned_money += current
            matecoin_account -= Decimal(sell)

    result_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as json_file:
        json.dump(result_dict, json_file, indent=2)
