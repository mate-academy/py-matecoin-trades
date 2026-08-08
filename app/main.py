import json
from decimal import Decimal


def calculate_profit(json_file: str) -> None:
    with open(json_file, "r") as trade_in:
        trades = json.load(trade_in)

    money_to_buy = Decimal("0")
    money_to_sell = Decimal("0")
    coin_now = Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            money_to_buy += bought * price
            coin_now += bought

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            price = Decimal(trade["matecoin_price"])
            money_to_sell += sold * price
            coin_now -= sold

    profit = {
        "earned_money": str(money_to_sell - money_to_buy),
        "matecoin_account": str(coin_now)
    }

    with open("profit.json", "w") as trades_out:
        json.dump(profit, trades_out, indent=2)
