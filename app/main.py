import json


def calculate_profit(trades_file: str) -> None:
    from decimal import Decimal

    with open(trades_file) as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = (
            Decimal(trade["bought"])
            if trade["bought"] is not None
            else Decimal("0")
        )
        sold = (
            Decimal(trade["sold"])
            if trade["sold"] is not None
            else Decimal("0")
        )
        price = Decimal(trade["matecoin_price"])

        earned_money += (sold - bought) * price
        matecoin_account += bought - sold

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
