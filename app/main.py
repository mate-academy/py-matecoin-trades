import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    matecoin_account = Decimal(0)
    earned_money = Decimal(0)
    with open(f"{file_name}", "r", encoding="utf-8") as file:
        trades = json.load(file)

    for trade in trades:
        bought = Decimal(trade.get("bought") or "0")
        sold = Decimal(trade.get("sold") or "0")
        price = Decimal(trade.get("matecoin_price") or "0")

        matecoin_account += bought - sold

        earned_money += (sold * price) - (bought * price)

    profit = {
        "earned_money": f"{earned_money}",
        "matecoin_account": f"{matecoin_account}"
    }

    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(profit, file, indent=2, ensure_ascii=False)
