import json
from decimal import Decimal, ROUND_HALF_UP


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as trade_file:
        trades = json.load(trade_file)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:

        if trade.get("bought"):
            matecoin_account += Decimal(trade["bought"])

        if trade.get("sold"):
            earned_money += \
                (
                    Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
                )

    earned_money = (
        earned_money.quantize(Decimal("0.00000001"), rounding=ROUND_HALF_UP))
    matecoin_account = (
        matecoin_account.quantize(
            Decimal("0.00000001"), rounding=ROUND_HALF_UP))

    result = {
        "earned_money": f"{earned_money: .8f}",
        "matecoin_account": f"{matecoin_account: .8f}"
    }

    with open("profit.json", "w") as profit_file:
        json.dump(result, profit_file, indent=4)
