import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(name_file) as file_read:
        trader_data = json.load(file_read)

    for elem in trader_data:
        if elem["bought"]:
            matcoin_value = Decimal(elem["bought"])
            matecoin_account += matcoin_value
            earned_money -= matcoin_value * Decimal(elem["matecoin_price"])

        if elem["sold"]:
            matcoin_value = Decimal(elem["sold"])
            matecoin_account -= matcoin_value
            earned_money += matcoin_value * Decimal(elem["matecoin_price"])

    result_dic = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file_write:
        json.dump(result_dic, file_write)
