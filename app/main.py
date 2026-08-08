import json
from decimal import Decimal


def calculate_profit(file_name):
    with open(file_name, "r") as file_trades:
        trades = json.load(file_trades)

    earned_money = 0
    matecoin_account = 0

    for entry in trades:
        matecoin_price = Decimal(entry["matecoin_price"])

        if entry["bought"]:
            earned_money -= Decimal(entry["bought"]) * matecoin_price
            matecoin_account += Decimal(entry["bought"])

        if entry["sold"]:
            earned_money += Decimal(entry["sold"]) * matecoin_price
            matecoin_account -= Decimal(entry["sold"])

    with open("profit.json", "w") as file_profit:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            file_profit,
            indent=2
        )


if __name__ == "__main__":
    calculate_profit("trades.json")
