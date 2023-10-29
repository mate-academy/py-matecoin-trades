import json

from decimal import Decimal


def calculate_profit(json_file: str) -> None:
    with open(json_file) as f:
        list_operations = json.load(f)

        matecoin_account = 0
        earned_money = 0

        for i in list_operations:
            if i["bought"]:
                earned_money -= (
                    Decimal(i["bought"])
                    * Decimal(i["matecoin_price"]))
                matecoin_account += Decimal(i["bought"])
            if i["sold"]:
                earned_money += (Decimal(i["sold"])
                                 * Decimal(i["matecoin_price"]))
                matecoin_account -= Decimal(i["sold"])

    value = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(value, f, indent=2)

#
# if __name__ == '__main__':
#     calculate_profit()
