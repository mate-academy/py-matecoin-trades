import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as json_file:
        trades: list[dict] = json.load(json_file)

    total_profit = Decimal("0.0")
    matecoin_balance = Decimal("0.0")

    for trade in trades:
        price_per_coin = Decimal(trade.get("matecoin_price"))
        bought = Decimal(trade.get("bought") or 0)
        sold = Decimal(trade.get("sold") or 0)
        transaction_profit = (sold * price_per_coin - bought * price_per_coin)
        total_profit += transaction_profit
        matecoin_balance += bought - sold

    with open("profit.json", "w") as profit_file:
        result = {
            "earned_money": str(total_profit),
            "matecoin_account": str(matecoin_balance),
        }
        json.dump(result, profit_file, indent=2)
