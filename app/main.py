import json
import decimal


def calculate_profit(filename: str) -> None:
    earned_money = decimal.Decimal(0)
    matecoin_account = decimal.Decimal(0)

    with open(filename, "r") as trades:
        data = json.load(trades)
        for trade in data:
            earned_money -= (
                decimal.Decimal(trade["bought"] or 0)
                * decimal.Decimal(trade["matecoin_price"])
            )

            earned_money += (
                decimal.Decimal(trade["sold"] or 0)
                * decimal.Decimal(trade["matecoin_price"])
            )

            matecoin_account += (
                decimal.Decimal(trade["bought"] or 0)
                - decimal.Decimal(trade["sold"] or 0)
            )
    with open("profit.json", "w") as profit:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account),
            },
            profit,
            indent=2,
        )
