import decimal
import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

trades_path = f"{BASE_DIR}/app/trades.json"
PROFIT = f"{BASE_DIR}/profit.json"


def calculate_profit(trades_path: str) -> None:

    with open(trades_path) as file_trades:
        trades = json.load(file_trades)

    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    for trade in trades:
        current_price = decimal.Decimal(trade["matecoin_price"])
        if trade["bought"]:
            current_bought = decimal.Decimal(trade["bought"])
            matecoin_account += current_bought
            earned_money -= current_bought * current_price
        if trade["sold"]:
            current_sold = decimal.Decimal(trade["sold"])
            matecoin_account -= current_sold
            earned_money += current_sold * current_price

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open(PROFIT, "w") as file_profit:
        json.dump(profit, file_profit, indent=2)
