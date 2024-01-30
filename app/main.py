from decimal import Decimal
import json


def calculate_profit(trades: str) -> None:
    with (open(trades, "r") as source_file):
        operations = json.load(source_file)

    earned_money = 0
    account = 0
    for trade in operations:
        currency = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            earned_money -= Decimal(trade["bought"]) * currency
            account += Decimal(trade["bought"])
        if trade["sold"]:
            earned_money += Decimal(trade["sold"]) * currency
            account -= Decimal(trade["sold"])
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
