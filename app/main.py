import json
import decimal


def calculate_profit(file_name: str) -> None:

    with open(file_name, "r") as file:
        trades = json.load(file)

    balance = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    for trade in trades:
        if trade["bought"]:
            balance["earned_money"] -= (
                decimal.Decimal(trade["bought"])
                * decimal.Decimal(trade["matecoin_price"])
            )

            balance["matecoin_account"] += decimal.Decimal(trade["bought"])
        if trade["sold"]:
            balance["earned_money"] += (
                decimal.Decimal(trade["sold"])
                * decimal.Decimal(trade["matecoin_price"])
            )

            balance["matecoin_account"] -= decimal.Decimal(trade["sold"])

    balance = {
        "earned_money": str(balance["earned_money"]),
        "matecoin_account": str(balance["matecoin_account"]),
    }

    with open("profit.json", "w") as file:
        json.dump(balance, file, indent=2)
