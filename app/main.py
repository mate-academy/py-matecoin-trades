import json

from decimal import Decimal


def calculate_profit(trade_file: str) -> None:
    with open(trade_file, "r") as trades_file:
        trades: list[dict] = json.load(trades_file)

    matecoin_account = Decimal(0)
    earned_money = Decimal(0)

    for trade in trades:
        if trade["bought"]:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
        if trade["sold"]:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))

    with open("profit.json", "w") as profit_file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account),
            },
            profit_file,
            indent=2,
        )
