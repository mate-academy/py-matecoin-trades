import json
from decimal import Decimal


def calculate_profit(trades_file: None) -> None:
    with open(trades_file) as f:
        trades = json.load(f)

    coin_account = Decimal("0")
    dollars_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"])
        sold = Decimal(trade["sold"])
        price = Decimal(trade["matecoin_price"])

        coin_account += bought - sold
        dollars_account -= bought * price
        dollars_account += sold * price

    result = {
        "coin_account": str(coin_account),
        "dollars_account": str(dollars_account),
        "profit": str(dollars_account + coin_account * price)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f)
