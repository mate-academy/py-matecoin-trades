import json
from pathlib import Path
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    BASE_DIR = Path(__file__).resolve().parent.parent
    TRADES = BASE_DIR / 'app' / 'trades.json'
    print(BASE_DIR)
    print(TRADES)
    account_data = {
        "earned_money": Decimal(0),
        "matecoin_account": Decimal(0),
    }

    with open(trades_file, "r") as file:
        data = json.load(file)

    for item in data:
        profit_in_matecoin = Decimal(item.get("bought") or 0) - Decimal(
            item.get("sold") or 0)
        profit_in_dollars = profit_in_matecoin * Decimal(
            item.get("matecoin_price"))
        account_data["earned_money"] -= profit_in_dollars
        account_data["matecoin_account"] += profit_in_matecoin

    account_data["earned_money"] = str(account_data["earned_money"])
    account_data["matecoin_account"] = str(account_data["matecoin_account"])

    with open("../profit.json", "w") as file:
        json.dump(account_data, file)
