import json
from decimal import Decimal
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PROFIT = f"{BASE_DIR}/profit.json"

def calculate_profit(trade_file: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(f"{trade_file}") as trades_json:
        trades = json.load(trades_json)

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            price_of_trade = Decimal(trade["bought"]) * matecoin_price
            earned_money -= price_of_trade
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"]:
            price_of_trade = Decimal(trade["sold"]) * matecoin_price
            earned_money += price_of_trade
            matecoin_account -= Decimal(trade["sold"])

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open(PROFIT, "w") as profit_json:
        json.dump(result, profit_json, indent=2)
