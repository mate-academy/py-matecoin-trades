from decimal import Decimal
import json


def calculate_profit(trades_json: str) -> None:
    with open(trades_json, "r") as file:
        trades = json.load(file)

    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            matecoin_account += Decimal(str(trade["bought"]))
            earned_money -= (
                Decimal(str(trade["bought"]))
                * Decimal(str(trade["matecoin_price"]))
            )

        if trade["sold"] is not None:
            matecoin_account -= Decimal(str(trade["sold"]))
            earned_money += (
                Decimal(str(trade["sold"]))
                * Decimal(str(trade["matecoin_price"]))
            )

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
