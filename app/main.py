import json
from decimal import Decimal, getcontext


def calculate_profit(file_name: None) -> None:
    getcontext().prec = 28

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(file_name, "r", encoding="utf-8") as f:
        trades = json.load(f)

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        bought = Decimal(trade["bought"]) \
            if trade["bought"] is not None else Decimal("0")
        sold = Decimal(trade["sold"]) \
            if trade["sold"] is not None else Decimal("0")

        earned_money -= bought * price
        matecoin_account += bought

        earned_money += sold * price
        matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
