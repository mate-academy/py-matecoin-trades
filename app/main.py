import json
from decimal import Decimal


def calculate_profit(input_file: str = "trades.json") -> None:
    with open(input_file, "r") as file:
        trades_data = json.load(file)
    earned_money = 0
    matecoin_account = 0
    for item in trades_data:
        if item["bought"] is not None:
            earned_money -= Decimal(item["bought"]) * (
                Decimal(item["matecoin_price"]))
            matecoin_account += Decimal(item["bought"])
        if item["sold"] is not None:
            earned_money += Decimal(item["sold"]) * (
                Decimal(item["matecoin_price"]))
            matecoin_account -= Decimal(item["sold"])

    dict_data = {"earned_money": str(earned_money),
                 "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as file1:
        json.dump(dict_data, file1, indent=2)
