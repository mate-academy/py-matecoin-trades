import json
from decimal import Decimal, ROUND_HALF_UP


def calculate_profit(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(str(trade["matecoin_price"]))

        if trade["bought"] is not None:
            bought = Decimal(str(trade["bought"]))
            matecoin_account += bought
            earned_money -= bought * price

        if trade["sold"] is not None:
            sold = Decimal(str(trade["sold"]))
            matecoin_account -= sold
            earned_money += sold * price

    precision = Decimal("0.00000001")

    result = {
        "earned_money": str(
            earned_money.quantize(precision, rounding=ROUND_HALF_UP)
        ),
        "matecoin_account": str(
            matecoin_account.quantize(precision, rounding=ROUND_HALF_UP)
        ),
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
