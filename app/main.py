import json
from decimal import Decimal
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def calculate_profit(file_name: str) -> None:
    matecoin_account = 0
    earned_money = 0
    with open(file_name, "r") as trade_json:
        trade_data = json.load(trade_json)
    for trade in trade_data:
        if not trade["bought"] is None:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= Decimal(trade["bought"]) *\
                Decimal(trade["matecoin_price"])
        if not trade["sold"] is None:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += Decimal(trade["sold"]) *\
                Decimal(trade["matecoin_price"])
    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open(f"{BASE_DIR}/profit.json", "w") as profit_json:
        json.dump(profit_data, profit_json, indent=2)
