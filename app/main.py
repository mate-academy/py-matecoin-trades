from decimal import Decimal
import json


def calculate_profit(trades_file: json) -> None:
    with open(trades_file) as trades_file:
        trades = json.load(trades_file)

    earned_money = 0
    matecoin_account = 0

    for trade in trades:
        if trade.get("bought"):
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account += Decimal(trade["bought"])

        if trade.get("sold"):
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
            matecoin_account -= Decimal(trade["sold"])

    with open("./profit.json", "w") as profit_file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            profit_file,
            indent=2
        )
