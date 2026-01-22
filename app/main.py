import json
from decimal import Decimal


def calculate_profit(file_name):
    earned_money = 0
    coins = 0
    with open(file_name) as f:
        trades = json.load(f)

    for i in trades:
        price = Decimal(i['matecoin_price'])
        if i["bought"]:
            earned_money -= Decimal(i["bought"]) * price
            coins += Decimal(i["bought"])
        if i["sold"]:
            earned_money += Decimal(i["sold"]) * price
            coins -= Decimal(i["sold"])

    add_profit = {"earned_money": f"{earned_money}",
                  "matecoin_account": f"{coins}"}

    with open("profit.json", "w") as f:
        json.dump(add_profit, f, indent=2)
