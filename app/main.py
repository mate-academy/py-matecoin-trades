import json
from decimal import Decimal
from pathlib import Path


def calculate_profit(trades: str) -> None:
    trades_path = Path(trades)
    profit_path = trades_path.parent.parent / "profit.json"

    with open(trades_path, "r") as f:
        data = json.load(f)

    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    for item in data:
        if item["bought"] is not None:
            bought = Decimal(item["bought"])
        else:
            bought = Decimal("0")

        if item["sold"] is not None:
            sold = Decimal(item["sold"])
        else:
            sold = Decimal("0")

        price = Decimal(item["matecoin_price"])
        matecoin_account += bought - sold
        earned_money += sold * price - bought * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open(profit_path, "w") as out:
        json.dump(result, out, indent=2)
