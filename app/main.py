import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        data = json.load(file)

        earned_money = Decimal(0)
        matacoin_account = Decimal(0)

        for ls in data:
            if ls["bought"]:
                earned_money -= Decimal(ls["bought"]) * Decimal(
                    ls["matecoin_price"])
                matacoin_account += Decimal(ls["bought"])
            if ls["sold"]:
                earned_money += Decimal(ls["sold"]) * Decimal(
                    ls["matecoin_price"])
                matacoin_account -= Decimal(ls["sold"])

        res = {"earned_money": str(earned_money),
               "matecoin_account": str(matacoin_account)}

    with open("profit.json", "w") as file_:
        json.dump(res, file_, indent=2)
