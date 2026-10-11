import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        trades_data = json.load(f)
        all_bought_money = Decimal("0")
        all_sold_money = Decimal("0")
        all_bought_coins = Decimal("0")
        all_sold_coins = Decimal("0")
        for trade_session in trades_data:
            price = Decimal(trade_session["matecoin_price"])
            if trade_session["bought"] is not None:
                bought = Decimal(trade_session["bought"])
                all_bought_money += bought * price
                all_bought_coins += bought
            if trade_session["sold"] is not None:
                sold = Decimal(trade_session["sold"])
                all_sold_money += sold * price
                all_sold_coins += sold
        earned_money = all_sold_money - all_bought_money
        matecoin_account = all_bought_coins - all_sold_coins
        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        with open("profit.json", "w") as f:
            json.dump(profit, f, indent=2)
