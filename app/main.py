from decimal import Decimal


import json


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        trades = json.load(f)

        earned_money = 0
        sum_of_coin = 0
        for trade in trades:
            if trade["bought"] is not None:
                sum_of_coin += Decimal(trade["bought"])
                earned_money -= (Decimal(trade["bought"])
                                 * Decimal(trade["matecoin_price"]))

            if trade["sold"] is not None:
                sum_of_coin -= Decimal(trade["sold"])
                earned_money += (Decimal(trade["sold"])
                                 * Decimal(trade["matecoin_price"]))

        profit = {"earned_money": str(earned_money),
                  "matecoin_account": str(sum_of_coin)}
        f.close()

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
        file.close()
