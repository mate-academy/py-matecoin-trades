import json
from decimal import Decimal


def calculate_profit(filename: str):
    with open(filename) as file_trades:
        trades = json.load(file_trades)

    earned_money = 0
    matecoin_account = 0

    for value in trades:
        matecoin_price = Decimal(value["matecoin_price"])

        if value["bought"]:
            earned_money -= Decimal(value["bought"]) * matecoin_price
            matecoin_account += Decimal(value["bought"])
        if value["sold"]:
            earned_money += Decimal(value["sold"]) * matecoin_price
            matecoin_account -= Decimal(value["sold"])

    with open("profit.json", "w") as file_profit:
        json.dump({
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }, file_profit, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
