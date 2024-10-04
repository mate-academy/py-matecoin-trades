import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        trades = json.load(json_file)
    earned_money = 0
    matecoin_account = 0
    for trade in trades:
        earned_money += (
            Decimal(trade["sold"] or "0") - Decimal(trade["bought"] or "0")
        ) * Decimal(trade["matecoin_price"])

        matecoin_account += Decimal(trade["bought"] or "0") - Decimal(
            trade["sold"] or "0"
        )

    with open("profit.json", "w") as profit_file:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account),
            },
            profit_file,
            indent=2,
        )
