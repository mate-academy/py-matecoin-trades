import json
from decimal import Decimal


def calculate_profit(file_name):
    with open(file_name, "r") as file_trades:
        trades = json.load(file_trades)

    earned_money = 0
    matecoin_account = 0

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade["bought"]:
            earned_money -= Decimal(trade["bought"]) * matecoin_price
            matecoin_account += Decimal(trade["bought"])

        elif trade["sold"]:
            earned_money += Decimal(trade["sold"]) * matecoin_price
            matecoin_account -= Decimal(trade["sold"])

    with open("profit.json", "w") as file_profit:
        json.dump(
            {"earned_money": str(earned_money),
             "matecoin_account": str(matecoin_account)},
            file_profit,
            indent=2
        )


if __name__ == "__main__":
    calculate_profit("trades.json")
