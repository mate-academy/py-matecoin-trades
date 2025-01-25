from decimal import Decimal

import json


def calculate_profit(trades_file_name: str) -> None:
    with open(trades_file_name) as trades_file:
        trades = json.load(trades_file)

    quantity_buy_matecoin = Decimal("0")
    total_usd_buy = Decimal("0")

    quantity_sell_matecoin = Decimal("0")
    total_usd_sell = Decimal("0")

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            quantity_buy_matecoin += bought
            total_usd_buy += matecoin_price * bought
        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            quantity_sell_matecoin += sold
            total_usd_sell += matecoin_price * sold

    earned_money = total_usd_sell - total_usd_buy
    matecoin_account = quantity_buy_matecoin - quantity_sell_matecoin

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit_data, profit_file, indent=2)
