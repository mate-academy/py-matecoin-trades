import json
import os
from decimal import Decimal
from pathlib import Path

BASE_DIR_PROFIT = Path(__file__).resolve().parent.parent
BASE_DIR_TRADES = Path(__file__).resolve().parent


def calculate_profit(file_name: str) -> None:
    file_path = os.path.join(BASE_DIR_TRADES, file_name)
    with open(file_path) as f:
        trades = json.load(f)

    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    for elem in trades:
        bought = Decimal(elem.get("bought") if elem.get("bought") else "0.0")
        sold = Decimal(elem.get("sold") if elem.get("sold") else "0.0")
        matecoin_price = Decimal(elem.get("matecoin_price", "0.0"))

        money_result = sold * matecoin_price - bought * matecoin_price
        matecoin_result = bought - sold

        earned_money += money_result
        matecoin_account += matecoin_result

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    profit_file_path = os.path.join(BASE_DIR_PROFIT, "profit.json")
    with open(profit_file_path, "w") as f:
        json.dump(profit, f, indent=2)


calculate_profit("trades.json")
