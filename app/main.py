import json
import os.path
from decimal import Decimal
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def calculate_profit(
        filepath: str = os.path.join(BASE_DIR, "app", "trades.json")
) -> None:
    with open(filepath, "r") as data_file:
        trades = json.load(data_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade.get("bought", 0) or 0)
        sold = Decimal(trade.get("sold", 0) or 0)
        matecoin_price = Decimal(trade.get("matecoin_price"))

        if bought > 0:
            earned_money -= bought * matecoin_price
            matecoin_account += bought
        if sold > 0:
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    result_path = os.path.join(BASE_DIR, "profit.json")
    with open(result_path, "w") as trade_result:
        json.dump(result, trade_result, indent=2)

    return None
