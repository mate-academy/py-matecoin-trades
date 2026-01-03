import json
import os
import decimal


def calculate_profit(trades_file: str) -> None:
    path = os.getcwd()
    path_read = os.path.join(path, "app", trades_file)
    path_write = os.path.join(path, "profit.json")

    with open(path_read, "r") as file:
        trades = json.load(file)

    earned_money = decimal.Decimal("0.0")
    matecoin_account = decimal.Decimal("0.0")

    for trade in trades:
        if not trade["sold"]:
            earned_money -= decimal.Decimal(trade["bought"]) \
                * decimal.Decimal(trade["matecoin_price"])
            matecoin_account += decimal.Decimal(trade["bought"])
        elif not trade["bought"]:
            earned_money += decimal.Decimal(trade["sold"]) \
                * decimal.Decimal(trade["matecoin_price"])
            matecoin_account -= decimal.Decimal(trade["sold"])
        else:
            earned_money += (
                decimal.Decimal(trade["sold"])
                - decimal.Decimal(trade["bought"])
            ) * decimal.Decimal(trade["matecoin_price"])
            matecoin_account += decimal.Decimal(trade["bought"]) \
                - decimal.Decimal(trade["sold"])

    profit_string = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open(path_write, "w") as file:
        json.dump(profit_string, file, indent=2)
