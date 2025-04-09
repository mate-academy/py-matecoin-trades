import json
from decimal import Decimal, getcontext


getcontext().prec = 30  # High precision for monetary calculations


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"]) \
            if trade["bought"] is not None else Decimal("0")
        sold = Decimal(trade["sold"]) \
            if trade["sold"] is not None else Decimal("0")
        price = Decimal(trade["matecoin_price"])

        if bought > 0:
            matecoin_account += bought
            earned_money -= bought * price

        if sold > 0:
            matecoin_account -= sold
            earned_money += sold * price

    result = {
        "earned_money": f"{earned_money:.7f}",
        "matecoin_account": f"{matecoin_account:.5f}"
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
