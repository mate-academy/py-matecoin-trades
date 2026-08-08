import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    purchases = Decimal(0)
    sales = Decimal(0)
    coins = Decimal(0)

    if filename.endswith(".json"):
        with open(filename, "r") as file:
            trades = json.load(file)
    else:
        with open(f"{filename}.json", "r") as file:
            trades = json.load(file)

    for trade in trades:
        if trade["bought"] is not None:
            coins += Decimal(trade["bought"])
            purchases += (Decimal(trade["bought"])
                          * Decimal(trade["matecoin_price"]))

        if trade["sold"] is not None:
            coins -= Decimal(trade["sold"])
            sales += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])

    profit = {
        "earned_money": str(sales - purchases),
        "matecoin_account": str(coins)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
