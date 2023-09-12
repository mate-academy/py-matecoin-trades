import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(name_file) as file_read:
        trader_data = json.load(file_read)

    for elem in trader_data:

        if elem["bought"]:
            matecoin_account += Decimal(elem["bought"])
            earned_money -= (Decimal(elem["bought"])
                             * Decimal(elem["matecoin_price"]))

        if elem["sold"]:
            matecoin_account -= Decimal(elem["sold"])
            earned_money += (Decimal(elem["sold"])
                             * Decimal(elem["matecoin_price"]))

    result_dic = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file_write:
        json.dump(result_dic, file_write, indent=2)
