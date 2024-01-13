import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    with open(name, "r") as file:
        trades_file = json.load(file)
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_file:
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            earned_money -= bought * matecoin_price
            matecoin_account += bought

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            earned_money += sold * matecoin_price
            matecoin_account -= sold
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)


# calculate_profit("trades.json")
