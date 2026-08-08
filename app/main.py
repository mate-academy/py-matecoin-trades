import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    with open(file_path, "r") as file:
        trades = json.load(file)

    balance_usd = Decimal("0")
    balance_coin = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade.get("bought") is not None:
            bought = Decimal(trade["bought"])
            balance_usd -= bought * price
            balance_coin += bought

        if trade.get("sold") is not None:
            sold = Decimal(trade["sold"])
            balance_usd += sold * price
            balance_coin -= sold

    result = {
        "earned_money": str(balance_usd),
        "matecoin_account": str(balance_coin)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
