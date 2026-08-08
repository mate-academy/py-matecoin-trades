import json
from decimal import Decimal
from pathlib import Path
from typing import Any


def calculate_profit(file_name: str) -> None:
    trades_path = Path(file_name).resolve()

    with open(trades_path, "r", encoding="utf-8") as input_file:
        trades: list[dict[str, Any]] = json.load(input_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought_amount = Decimal(trade["bought"])
            earned_money -= bought_amount * price
            matecoin_account += bought_amount

        if trade["sold"] is not None:
            sold_amount = Decimal(trade["sold"])
            earned_money += sold_amount * price
            matecoin_account -= sold_amount

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    output_path = trades_path.parent.parent / "profit.json"

    with open(output_path, "w", encoding="utf-8") as output_file:
        json.dump(result, output_file, indent=2)
