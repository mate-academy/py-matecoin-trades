import json
from decimal import Decimal


def calculate_profit(trades_file: any) -> None:
    with open(trades_file, "r") as base_file, open(
        "profit.json", "w"
    ) as new_file:
        trades = json.load(base_file)
        transaction = {
            "earned_money": Decimal(0),
            "matecoin_account": Decimal(0),
        }

        for trade in trades:
            if trade["bought"]:
                transaction["earned_money"] -= Decimal(
                    trade["bought"]
                ) * Decimal(trade["matecoin_price"])
                transaction["matecoin_account"] += Decimal(trade["bought"])
            if trade["sold"]:
                transaction["earned_money"] += Decimal(
                    trade["sold"]
                ) * Decimal(trade["matecoin_price"])
                transaction["matecoin_account"] -= Decimal(trade["sold"])
        json.dump(
            {
                "earned_money": str(transaction["earned_money"]),
                "matecoin_account": str(transaction["matecoin_account"]),
            },
            new_file,
            indent=2,
        )
