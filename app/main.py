import json
from decimal import Decimal


def calculate_profit(trades_json_file_name: str) -> None:
    with open(trades_json_file_name, "r") as file:
        trades = json.load(file)
    balance = Decimal("0")
    temp = Decimal("0")
    for trade in trades:
        if trade["bought"]:
            balance += Decimal(trade["bought"])
            temp -= Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
        if trade["sold"]:
            balance -= Decimal(trade["sold"])
            temp += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])

    result = {"earned_money": str(temp),
              "matecoin_account": str(balance)}

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
