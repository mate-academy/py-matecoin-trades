import json
import sys
from decimal import Decimal


def calculate_profit(trades_file_name: str) -> None:
    with open(trades_file_name) as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            matecoin_account += Decimal(trade["bought"])
            earned_money -=\
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])

        if trade["sold"] is not None:
            matecoin_account -= Decimal(trade["sold"])
            earned_money +=\
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])

    profit = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)


if __name__ == "__main__":
    calculate_profit(sys.argv[1])
