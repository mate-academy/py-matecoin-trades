import json
from decimal import Decimal
from pathlib import Path
from typing import Any, Dict, List


def calculate_profit(
        trades_file: str,
        output_file: str = "profit.json"
) -> None:

    trades_path = Path(trades_file)
    output_path = Path(output_file)

    with trades_path.open("r", encoding="utf-8") as file:
        trades: List[Dict[str, Any]] = json.load(file)

    earned_money: Decimal = Decimal("0")
    matecoin_account: Decimal = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade.get("bought") is not None:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * price

        if trade.get("sold") is not None:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with output_path.open("w", encoding="utf-8") as file:
        json.dump(result, file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
