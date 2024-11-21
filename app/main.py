import json
from decimal import Decimal


def calculate_profit(trades_json: str) -> None:
    with open(trades_json, "r") as file:
        trades = json.load(file)
    profit = Decimal("0")
    account = Decimal("0")
    for trade in trades:
        if trade["bought"]:
            profit -= (Decimal(trade["bought"])
                       * Decimal(trade["matecoin_price"]))
            account += Decimal(trade["bought"])
        if trade["sold"]:
            profit += (Decimal(trade["sold"])
                       * Decimal(trade["matecoin_price"]))
            account -= Decimal(trade["sold"])
    result = {
        "earned_money": str(profit),
        "matecoin_account": str(account)
    }
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
