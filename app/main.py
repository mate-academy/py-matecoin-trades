from decimal import Decimal
import json


def calculate_profit(trades_file: str) -> None:
    with open(trades_file) as f:
        trades = json.load(f)

    earned_money = 0
    matecoin_account = 0

    for trade in trades:
        if trade["bought"] is None:
            trade["bought"] = 0
        elif trade["sold"] is None:
            trade["sold"] = 0
        dif = Decimal(Decimal(trade["bought"]) - Decimal(trade["sold"]))
        earned_money += dif * Decimal(trade["matecoin_price"])
        matecoin_account += Decimal(dif)
    with open("profit.json", "w") as f:
        json.dump(
            {
                "earned_money": str(- earned_money),
                "matecoin_account": str(matecoin_account
                                        )}, f, indent=2, )
