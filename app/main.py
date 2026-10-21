import json
from decimal import Decimal
from pathlib import Path


def calculate_profit(file_name: str) -> None:
    """Calculate the result of Matecoin trades and save it to profit.json."""
    with open(file_name) as trades_file:
        trades = json.load(trades_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        bought = Decimal(trade["bought"] or "0")
        sold = Decimal(trade["sold"] or "0")

        matecoin_account += bought - sold
        earned_money += (sold - bought) * price

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    output_file = Path(file_name).resolve().parent.parent / "profit.json"
    with open(output_file, "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
