import decimal
import json


def calculate_profit(name_file: str) -> None:
    with open(name_file,) as f:
        coin_data = json.load(f)

    earned_money = decimal.Decimal(0)
    matecoin_account = decimal.Decimal(0)

    for i in coin_data:
        if i["bought"]:
            matecoin_account += decimal.Decimal(i["bought"])
            earned_money -= (decimal.Decimal(i["bought"])
                             * decimal.Decimal(i["matecoin_price"]))
        if i["sold"]:
            matecoin_account -= decimal.Decimal(i["sold"])
            earned_money += (decimal.Decimal(i["sold"])
                             * decimal.Decimal(i["matecoin_price"]))

    dict_coin = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as k:
        json.dump(dict_coin, k, indent=2)
