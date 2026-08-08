import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as trades1:
        data_python = json.load(trades1)
        data = {"earned_money": Decimal("0"), "matecoin_account": Decimal("0")}
        for i in data_python:
            price = Decimal(i["matecoin_price"])
            if i["bought"] is None:
                pass
            else:
                bought = Decimal(i["bought"])
                earned_money = bought * price
                data["earned_money"] -= earned_money
                data["matecoin_account"] += bought

            if i["sold"] is None:
                pass
            else:
                sold = Decimal(i["sold"])
                earned_money1 = sold * price
                data["earned_money"] += earned_money1
                data["matecoin_account"] -= sold
        str_earned_money = str(data["earned_money"])
        str_matecoin_account = str(data["matecoin_account"])
        data["earned_money"] = str_earned_money
        data["matecoin_account"] = str_matecoin_account
    with open("profit.json", "w") as file:
        json.dump(data, file, indent=2)
