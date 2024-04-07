import os
import json
from decimal import Decimal
from typing import List, Dict


def calculate_profit(trades_file: str) -> None:
    """
    Calculate profit from trades and save the result in profit.json file.

    Args:
        trades_file (str): The file path containing trades information
        in JSON format.
    """
    script_dir = os.path.dirname(__file__)
    trades_file_path = os.path.join(script_dir, trades_file)

    with open(trades_file_path, "r") as f:
        trades: List[Dict[str, str]] = json.load(f)

    earned_money: Decimal = Decimal("0")
    matecoin_account: Decimal = Decimal("0")

    for trade in trades:
        bought_amount: Decimal = Decimal(trade.get("bought", "0") or "0")
        sold_amount: Decimal = Decimal(trade.get("sold", "0") or "0")
        matecoin_price: Decimal = Decimal(trade["matecoin_price"])

        earned_money -= bought_amount * matecoin_price
        matecoin_account += bought_amount

        earned_money += sold_amount * matecoin_price
        matecoin_account -= sold_amount

    profit_data: Dict[str, str] = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit_data, f, indent=2)


calculate_profit("trades.json")
