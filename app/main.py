from decimal import Decimal
import json


def calculate_profit(trades: str) -> None:
    with (open(trades, "r") as trade_info):
        my_trades = json.load(trade_info)
        profit = 0
        quantity = 0
        for coin in my_trades:
            sold = coin["sold"]
            bought = coin["bought"]
            price = Decimal(coin["matecoin_price"])
            if sold is None:
                sold = 0
            if bought is None:
                bought = 0
            profit += (Decimal(bought) * price) - (Decimal(sold) * price)
            quantity += (Decimal(bought) - Decimal(sold))

        result = {
            "earned_money": str(-profit),
            "matecoin_account": str(quantity)
        }
    with open("profit.json", "w", ) as profit:
        json.dump(result, profit, indent=2)
