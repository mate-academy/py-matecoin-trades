from decimal import Decimal
import json
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent


TRADES = f"{BASE_DIR}/app/trades.json"
PROFIT = f"{BASE_DIR}/profit.json"


def calculate_profit(filename: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    try:
        with open(filename, "r") as f:
            content = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        content = []
    if isinstance(content, dict):
        earned_money = Decimal(str(content.get("earned_money", "0")))
        matecoin_account = Decimal(str(content.get("matecoin_account", "0")))
        trades = content.get("trades", [])
    elif isinstance(content, list):
        trades = content
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
        "matecoin_account": str(matecoin_account)}
    with open(PROFIT, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
