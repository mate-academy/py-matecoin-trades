import json
from decimal import Decimal
from json import JSONDecodeError

PROFIT = "profit.json"

def calculate_profit(filename: str) -> None:
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")

    # --- читаємо файл ---
    try:
        with open(filename, "r") as file:
            content = file.read().strip()
            if not content:
                trades_data = []
            else:
                trades_data = json.loads(content)
    except (JSONDecodeError, FileNotFoundError):
        trades_data = []

    # --- обробка словника з попередніми значеннями ---
    if isinstance(trades_data, dict):
        earned_money = Decimal(trades_data.get("earned_money", "0"))
        matecoin_account = Decimal(trades_data.get("matecoin_account", "0"))
        trades = trades_data.get("trades", [])
    elif isinstance(trades_data, list):
        trades = trades_data
    else:
        trades = []

    # --- обчислення прибутку ---
    for trade in trades:
        price = Decimal(str(trade.get("matecoin_price") or "0"))

        if trade.get("bought") not in (None, ""):
            bought = Decimal(str(trade.get("bought")))
            matecoin_account += bought
            earned_money -= bought * price

        if trade.get("sold") not in (None, ""):
            sold = Decimal(str(trade.get("sold")))
            matecoin_account -= sold
            earned_money += sold * price

    # --- запис результату ---
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open(PROFIT, "w") as file:
        json.dump(result, file, indent=2)
