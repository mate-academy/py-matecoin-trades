import json
from decimal import Decimal


def calculate_profit(name_of_the_file: str) -> None:

    with open(name_of_the_file) as f:
        trades = json.load(f)

    buy_in_dollars = Decimal("0.0")
    sell_in_dollars = Decimal("0.0")

    buy_in_matecoin = Decimal("0.0")
    sell_in_matecoin = Decimal("0.0")

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])

        bought = (Decimal(trade["bought"])
                  if trade["bought"] else Decimal("0.0"))
        sold = (Decimal(trade["sold"])
                if trade["sold"] else Decimal("0.0"))

        buy_in_matecoin += bought
        sell_in_matecoin += sold

        bought_in_dollars = bought * matecoin_price
        sold_in_dollars = sold * matecoin_price

        buy_in_dollars += bought_in_dollars
        sell_in_dollars += sold_in_dollars

    earned_money = sell_in_dollars - buy_in_dollars
    matecoin_account = buy_in_matecoin - sell_in_matecoin

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
