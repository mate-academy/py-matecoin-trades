import json
from _decimal import Decimal


def calculate_profit(trades_path: str) -> None:
    with (
        open(trades_path, "r") as trades_file,
        open("profit.json", "w") as profit_file
    ):
        trades = json.load(trades_file)
        profit = {
            "earned_money": Decimal("0"),
            "matecoin_account": Decimal("0")
        }

        for trade in trades:
            if trade["bought"]:
                bought = Decimal(trade["bought"])
            else:
                bought = Decimal("0")
            sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
            price = Decimal(trade["matecoin_price"])

            profit["matecoin_account"] += bought - sold
            profit["earned_money"] += sold * price - bought * price

        profit_str = {
            "earned_money": str(profit["earned_money"]),
            "matecoin_account": str(profit["matecoin_account"])
        }

        json.dump(profit_str, profit_file, indent=2)
