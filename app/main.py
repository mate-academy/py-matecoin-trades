import json
from decimal import Decimal


def calculate_profit(exchange: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    with open(exchange, "r") as f:
        trades = json.load(f)

    for trade in trades:
        if trade["bought"] is not None:
            bought_matecoin = Decimal(trade["bought"])
            price_matecoin = Decimal(trade["matecoin_price"])
            earned_money -= bought_matecoin * price_matecoin
            matecoin_account += bought_matecoin
        if trade["sold"] is not None:
            sold_matecoin = Decimal(trade["sold"])
            price_matecoin = Decimal(trade["matecoin_price"])
            earned_money += sold_matecoin * price_matecoin
            matecoin_account -= sold_matecoin

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as result_trade:
        json.dump(result, result_trade, indent=2)
