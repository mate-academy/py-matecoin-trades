import json
from decimal import Decimal
from pathlib import Path


def calculate_profit(trades: str) -> None:
    with open(trades) as json_trades:
        trades_data = json.load(json_trades)

    earned = Decimal("0")
    matecoins = Decimal("0")

    for trade in trades_data:
        if trade["sold"]:
            earned += (Decimal(trade["sold"])
                       * Decimal(trade["matecoin_price"]))
            matecoins -= Decimal(trade["sold"])
        if trade["bought"]:
            earned -= (Decimal(trade["bought"])
                       * Decimal(trade["matecoin_price"]))
            matecoins += Decimal(trade["bought"])

    profit = {
        "earned_money": str(earned),
        "matecoin_account": str(matecoins)
    }
    path = f"{Path(__file__).resolve().parent.parent}/profit.json"
    with open(path, "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
