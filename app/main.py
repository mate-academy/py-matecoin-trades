import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    profit_data = {"earned_money": 0, "matecoin_account": 0}

    with (open(file_name, "r") as trades_file,
          open("profit.json", "w") as profit_file):

        trades_data = json.load(trades_file)

        for trade in trades_data:
            if trade["bought"]:
                profit_data["earned_money"] -= (
                    Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
                )

                profit_data["matecoin_account"] += Decimal(trade["bought"])

            if trade["sold"]:
                profit_data["earned_money"] += (
                    Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
                )

                profit_data["matecoin_account"] -= Decimal(trade["sold"])

        profit_data["earned_money"] = str(profit_data["earned_money"])
        profit_data["matecoin_account"] = str(profit_data["matecoin_account"])

        json.dump(profit_data, profit_file, indent=2)
