from decimal import Decimal
import json


def calculate_profit(trades_json: str) -> None:
    with open(trades_json, "r") as f:
        trade_info = json.load(f)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for trade in trade_info:
        if trade["bought"] is not None:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= (Decimal(trade["bought"])) * \
                            (Decimal(trade["matecoin_price"]))
        if trade["sold"] is not None:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += (Decimal(trade["sold"])) * \
                            (Decimal(trade["matecoin_price"]))

    profit_json = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as t:
        json.dump(profit_json, t, indent=2)
