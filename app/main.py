import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as json_file:
        trades_json = json.load(json_file)

    mate_coin_account = 0
    bought = 0
    sold = 0

    for trade in trades_json:
        if trade["bought"] is not None:
            bought += (
                Decimal(trade["matecoin_price"]) * Decimal(trade["bought"])
            )
            mate_coin_account += Decimal(trade["bought"])

        if trade["sold"] is not None:
            sold += (
                Decimal(trade["matecoin_price"]) * Decimal(trade["sold"])
            )
            mate_coin_account -= Decimal(trade["sold"])

    profit_mate_coin = {
        "earned_money": str(Decimal(sold) - Decimal(bought)),
        "matecoin_account": str(mate_coin_account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit_mate_coin, profit_file, indent=2)
