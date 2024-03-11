import json
from decimal import Decimal
from pathlib import Path


def calculate_profit(filename: str = "trades.json") -> None:
    with open(filename, "r") as f:
        trades = json.load(f, parse_float=Decimal)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        # Directly handle None cases and ensure Decimal is used without falling back to float
        bought = Decimal(trade.get("bought") or "0")
        sold = Decimal(trade.get("sold") or "0")
        matecoin_price = Decimal(trade["matecoin_price"])
        matecoin_account += bought - sold
        earned_money += (sold - bought) * matecoin_price

    result = {
        "earned_money": str(earned_money.normalize()),
        "matecoin_account": str(matecoin_account.normalize())
    }

    current_directory = Path.cwd()
    profit_file_path = current_directory / "profit.json"

    with open(profit_file_path, "w) as f:
        json.dump(result, f, indent=2)
