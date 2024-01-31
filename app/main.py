import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    total_profit = Decimal("0.0000000000")
    matecoin_account = Decimal("0.0000000000")

    with open(filename, "r") as file:
        trades = json.load(file)

        for trade in trades:
            bought = Decimal(
                trade["bought"]
            ) if trade["bought"] else Decimal("0")
            sold = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
            price = Decimal(trade["matecoin_price"])

            matecoin_account += bought - sold

            if bought:
                total_profit -= bought * price
            if sold:
                total_profit += sold * price

    total_profit_str = f"{total_profit:.10f}".rstrip("0").rstrip(".")
    matecoin_account_str = f"{matecoin_account:.10f}".rstrip("0").rstrip(".")

    profit_data = {
        "earned_money": total_profit_str,
        "matecoin_account": matecoin_account_str
    }

    with open("profit.json", "w") as outfile:
        json.dump(profit_data, outfile, indent=2)
