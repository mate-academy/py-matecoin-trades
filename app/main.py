import json
from decimal import Decimal, getcontext


# Set precision high enough for crypto calculations
getcontext().prec = 28


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"]) if trade["bought"] else Decimal("0")
        sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        price = Decimal(trade["matecoin_price"])

        if bought > 0:
            # When buying: spend money, increase coin balance
            earned_money -= bought * price
            matecoin_account += bought

        if sold > 0:
            # When selling: get money, decrease coin balance
            earned_money += sold * price
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as output:
        json.dump(result, output, indent=2)
