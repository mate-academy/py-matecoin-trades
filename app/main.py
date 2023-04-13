from __future__ import annotations
import json
import decimal


def calculate_profit(trades_file: json) -> None:
    with open(trades_file) as f:
        trades = json.load(f)

    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")
    for trade in trades:
        matecoin_price = decimal.Decimal(trade.get("matecoin_price"))
        if trade.get("bought") is not None:
            bought = decimal.Decimal(trade["bought"])
            earned_money -= bought * matecoin_price
            matecoin_account += bought
        if trade["sold"] is not None:
            sold = decimal.Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * matecoin_price
    with open("profit.json", "w") as file:
        json.dump({"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)},
                  file, indent=2,)
