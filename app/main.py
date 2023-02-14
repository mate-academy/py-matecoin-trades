import json
from decimal import Decimal


def calculate_profit(file_: str) -> None:
    with (
        open(file_, "r") as trades_file,
        open("profit.json", "w") as profit_file
    ):
        trades = json.load(trades_file)

        profit = {
            "earned_money": "0",
            "matecoin_account": "0"
        }

        for deal in trades:
            if deal["bought"] is not None:
                profit["matecoin_account"] = str(
                    Decimal(profit["matecoin_account"])
                    + Decimal(deal["bought"])
                )
                profit["earned_money"] = str(
                    Decimal(profit["earned_money"])
                    - (
                        Decimal(deal["bought"])
                        * Decimal(deal["matecoin_price"])
                    )
                )

            if deal["sold"] is not None:
                profit["matecoin_account"] = str(
                    Decimal(profit["matecoin_account"]) - Decimal(deal["sold"])
                )
                profit["earned_money"] = str(
                    Decimal(profit["earned_money"])
                    + (Decimal(deal["sold"]) * Decimal(deal["matecoin_price"]))
                )
        json.dump(profit, profit_file, indent=2)
