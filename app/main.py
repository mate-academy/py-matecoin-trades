import json
from decimal import Decimal, ROUND_HALF_UP


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades = json.load(f)

    total_bought = Decimal("0")
    total_sold = Decimal("0")
    total_coin_buy = Decimal("0")
    total_coin_sold = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            total_coin_buy += amount
            total_bought += amount * price

        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            total_coin_sold += amount
            total_sold += amount * price

    earned = (total_sold - total_bought).quantize(Decimal("0.0000001"),
                                                  rounding=ROUND_HALF_UP)
    balance = (total_coin_buy - total_coin_sold).quantize(
        Decimal("0.00001"), rounding=ROUND_HALF_UP
    )

    profit = {"earned_money": str(earned), "matecoin_account": str(balance)}

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
