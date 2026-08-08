import json

from decimal import Decimal


def calculate_profit(name: str) -> None:
    new_dict = {}
    earned_money = 0
    matecoin_account = 0

    with open(name, "r") as file, open("profit.json", "w") as result:
        data = json.load(file)
        for dictionary in data:
            for key in dictionary:

                if key == "bought" and dictionary["bought"] is not None:
                    matecoin_account += Decimal(dictionary["bought"])
                    earned_money -= Decimal(dictionary["bought"]) \
                        * Decimal(dictionary["matecoin_price"])

                if key == "sold" and dictionary["sold"] is not None:
                    matecoin_account -= Decimal(dictionary["sold"])
                    earned_money += Decimal(dictionary["sold"]) \
                        * Decimal(dictionary["matecoin_price"])

        new_dict["earned_money"] = str(earned_money)
        new_dict["matecoin_account"] = str(matecoin_account)

        json.dump(new_dict, result, indent=2)
