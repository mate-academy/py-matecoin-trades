import decimal

import json


def calculate_profit(file_name: str) -> None:
    result_dict = {}
    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")
    with open(file_name) as f:
        content = json.load(f)
        for el in content:
            dec_price = decimal.Decimal(el["matecoin_price"])
            if el["bought"] and el["bought"] != "null":
                dec_bought = decimal.Decimal(el["bought"])
                earned_money -= dec_bought * dec_price
                matecoin_account += dec_bought
            if el["sold"] and el["sold"] != "null":
                dec_sold = decimal.Decimal(el["sold"])
                earned_money += dec_sold * dec_price
                matecoin_account -= dec_sold
    result_dict["earned_money"] = str(earned_money)
    result_dict["matecoin_account"] = str(matecoin_account)
    with open("profit.json", "w") as a:
        json.dump(result_dict, a, indent=2)
