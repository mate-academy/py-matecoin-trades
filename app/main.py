import json
from decimal import Decimal
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = Path(__file__).resolve().parent.parent

TRADES = f"{BASE_DIR}/app/trades.json"
PROFIT = f"{BASE_DIR}/profit.json"


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as json_file:
        content = json.load(json_file)

        if isinstance(content, dict):
            earned_money = Decimal(content.get("earned_money", "0"))
            matecoin_account = Decimal(content.get("matecoin_account", "0"))
            trades = content.get("trades", [])
        elif isinstance(content, list):
            trades = content
            earned_money = Decimal("0")
            matecoin_account = Decimal("0")
        else:
            trades = []

        for trade in trades:
            price = Decimal(str(trade.get("matecoin_price") or "0"))
            if trade.get("bought") not in (None, ""):
                bought = Decimal(str(trade.get("bought")))
                earned_money -= bought * price
                matecoin_account += bought

            if trade.get("sold") not in (None, ""):
                sold = Decimal(str(trade.get("sold")))
                earned_money += sold * price
                matecoin_account -= sold

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }

        with open("profit.json", "w") as json_file:
            json.dump(result, json_file, indent=2, ensure_ascii=False)

    for trade in trades:
        price = Decimal(str(trade.get("matecoin_price") or "0"))
        if trade.get("bought") not in (None, ""):
            bought = Decimal(str(trade.get("bought")))
            earned_money -= bought * price
            matecoin_account += bought

        if trade.get("sold") not in (None, ""):
            sold = Decimal(str(trade.get("sold")))
            earned_money += sold * price
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as json_file:
        json.dump(result, json_file, indent=2, ensure_ascii=False)
