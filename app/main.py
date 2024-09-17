import json
from decimal import Decimal


def calculate_profit(trades_file_name: str) -> None:
    with (
        open(trades_file_name, "r") as trades_file,
        open("profit.json", "w") as profit_file
    ):
        trades = json.load(trades_file)

        matecoin_account = 0
        profit = 0
        for trade in trades:
            bought = (
                Decimal(trade["bought"])
                if trade["bought"]
                else Decimal("0")
            )
            sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
            price = Decimal(trade["matecoin_price"])

            matecoin_account += bought - sold
            profit += sold * price - bought * price

        json.dump(
            {
                "earned_money": f"{profit}",
                "matecoin_account": f"{matecoin_account}"
            },
            profit_file,
            indent=2
        )
