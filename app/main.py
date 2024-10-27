import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        data_from_file = json.load(file)

    how_many_left, money = Decimal("0"), Decimal("0")

    for one in data_from_file:
        if one["bought"]:
            money -= Decimal(one["bought"]) * Decimal(one["matecoin_price"])
            how_many_left += Decimal(one["bought"])
        if one["sold"]:
            money += Decimal(one["sold"]) * Decimal(one["matecoin_price"])
            how_many_left -= Decimal(one["sold"])

    our_res = {"earned_money": str(money),
               "matecoin_account": str(how_many_left)}

    with open("profit.json", "w") as file_for_res:
        json.dump(our_res, file_for_res, indent=2)
