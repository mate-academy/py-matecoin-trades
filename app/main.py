from __future__ import annotations
import json
from decimal import Decimal


def calculate_profit(trades_file: json) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for data_trades in trades:
        if data_trades.get("bought"):
            bought = Decimal(data_trades["bought"])
            mate_coin = Decimal(data_trades["matecoin_price"])
            earned_money -= bought * mate_coin
            matecoin_account += bought
        if data_trades.get("sold"):
            sold = Decimal(data_trades["sold"])
            mate_coin = Decimal(data_trades["matecoin_price"])
            earned_money += sold * mate_coin
            matecoin_account -= sold

    with open("profit.json", "w") as file:
        json.dump({"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)},
                  file, indent=2,)
