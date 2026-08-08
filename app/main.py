import json
from decimal import Decimal


def calculate_profit(name_of_the_file: str) -> None:
    with open(name_of_the_file, "r") as file:
        ls = json.load(file)

    money = 0
    account = 0

    for i in ls:
        if i["sold"] is None:
            i["sold"] = 0
        if i["bought"] is None:
            i["bought"] = 0

        bought = Decimal(i["sold"]) - Decimal(i["bought"])
        account -= bought
        money += Decimal(i["matecoin_price"]) * bought

    profit = {"earned_money": str(money), "matecoin_account": str(account)}

    with open("profit.json", "w") as new_file:
        json.dump(profit, new_file, indent=2)
