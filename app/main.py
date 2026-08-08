import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    with open(file_name) as f:
        money = 0
        coin = 0
        for i in json.load(f):
            if i["bought"] and i["sold"]:
                money -= Decimal(i["bought"]) * Decimal(i["matecoin_price"])
                money += Decimal(i["sold"]) * Decimal(i["matecoin_price"])
                coin -= Decimal(i["sold"])
                coin += Decimal(i["bought"])
            if i["bought"] and not i["sold"]:
                money -= Decimal(i["bought"]) * Decimal(i["matecoin_price"])
                coin += Decimal(i["bought"])
            if i["sold"] and not i["bought"]:
                money += Decimal(i["sold"]) * Decimal(i["matecoin_price"])
                coin -= Decimal(i["sold"])
        res_dict = {
            "earned_money": str(money),
            "matecoin_account": str(coin)
        }
        with open("profit.json", "w") as fl:
            json.dump(res_dict, fl, indent=2)
