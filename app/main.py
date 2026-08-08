from decimal import Decimal, ROUND_HALF_UP
import json


def calculate_profit(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(str(trade["matecoin_price"]))

        if trade["bought"] is not None:
            amount = Decimal(str(trade["bought"]))
            earned_money -= amount * price
            matecoin_account += amount
        if trade["sold"] is not None:
            amount = Decimal(str(trade["sold"]))
            earned_money += amount * price
            matecoin_account -= amount

    earned_money = earned_money.quantize(
        Decimal("0.00000001"), rounding=ROUND_HALF_UP)
    matecoin_account = matecoin_account.quantize(
        Decimal("0.00001"), rounding=ROUND_HALF_UP)

    earned_money_str = format(earned_money.normalize(), "f")
    matecoin_account_str = format(matecoin_account.normalize(), "f")

    result = {
        "earned_money": earned_money_str,
        "matecoin_account": matecoin_account_str
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
