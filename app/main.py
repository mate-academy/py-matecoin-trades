import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    data = []
    spend = Decimal("0")
    earned = Decimal("0")
    account = Decimal("0")

    with open(trades_file, "r") as file:
        data = json.load(file)

    for trade in data:
        if trade["bought"]:
            spend += (Decimal(trade["bought"])
                      * Decimal(trade["matecoin_price"]))
            account += Decimal(trade["bought"])
        if trade["sold"]:
            earned += (Decimal(trade["sold"])
                       * Decimal(trade["matecoin_price"]))
            account -= Decimal(trade["sold"])

    result = {
        "earned_money": str(earned - spend),
        "matecoin_account": str(account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
