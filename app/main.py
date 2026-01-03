import json
from decimal import Decimal
from typing import Optional, TypedDict


class Trade(TypedDict):
    bought: Optional[str]
    sold: Optional[str]
    matecoin_price: str


def calculate_profit(
    trades_filename: str,
    report_filename: str = "profit.json",
) -> None:
    usd_profit = Decimal("0")
    matecoin_balance = Decimal("0")

    with open(trades_filename, "r", encoding="utf-8") as trades_file:
        trades: list[Trade] = json.load(trades_file)

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            amount = Decimal(trade["bought"])
            matecoin_balance += amount
            usd_profit -= amount * price

        if trade["sold"] is not None:
            amount = Decimal(trade["sold"])
            matecoin_balance -= amount
            usd_profit += amount * price

    report_data = {
        "earned_money": str(usd_profit),
        "matecoin_account": str(matecoin_balance),
    }

    with open(report_filename, "w", encoding="utf-8") as report_file:
        json.dump(report_data, report_file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
