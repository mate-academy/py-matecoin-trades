import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(file_name) as f:
        trades = json.load(f)
        for trade in trades:
            if not trade["bought"] is None:
                earned_money -= Decimal(trade["bought"]
                                        ) * Decimal(trade["matecoin_price"])
                matecoin_account += Decimal(trade["bought"])
            if not trade["sold"] is None:
                earned_money += Decimal(trade["sold"]
                                        ) * Decimal(trade["matecoin_price"])
                matecoin_account -= Decimal(trade["sold"])
    with open("profit.json", "w") as f_out:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            f_out,
            indent=2
        )
