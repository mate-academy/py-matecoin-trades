import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    profit = {"earned_money": Decimal(0),
              "matecoin_account": Decimal(0)
              }
    with open(file_name, "r") as trades:
        for item in json.load(trades):
            if item["bought"]:
                bought = Decimal(item["bought"])
                matecoin_price = Decimal(item["matecoin_price"])

                profit["earned_money"] -= bought * matecoin_price
                profit["matecoin_account"] += Decimal(item["bought"])
            if item["sold"]:
                sold = Decimal(item["sold"])
                matecoin_price = Decimal(item["matecoin_price"])

                profit["earned_money"] += sold * matecoin_price
                profit["matecoin_account"] -= Decimal(item["sold"])

    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])

    with open("profit.json", "w") as result:
        json.dump(profit, result, indent=2)
