import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    money_res = 0
    coins_res = 0

    with open(filename) as file_opened:
        file_data = json.load(file_opened)

    for el in file_data:
        purchased_amount = 0

        if el["bought"] is not None:
            purchased_amount += Decimal(el["bought"])
        if el["sold"] is not None:
            purchased_amount -= Decimal(el["sold"])

        money_res += (purchased_amount * -1) * Decimal(el["matecoin_price"])
        coins_res += purchased_amount

    with open("profit.json", "w+") as curr_file:
        json.dump({
            "earned_money": str(money_res),
            "matecoin_account": str(coins_res)
        }, curr_file, indent=2)
