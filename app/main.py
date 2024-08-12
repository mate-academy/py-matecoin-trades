import json
from decimal import Decimal


def calculate_profit(trades_info: str) -> None:
    with open(trades_info, "r") as f:
        trades = json.load(f)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:
        bought = trade["bought"]
        sold = trade["sold"]
        matecoin_price = trade["matecoin_price"]

        if bought:
            bought_amount = Decimal(bought)
            matecoin_account += bought_amount
            earned_money -= bought_amount * Decimal(matecoin_price)

        if sold:
            sold_amount = Decimal(sold)
            matecoin_account -= sold_amount
            earned_money += sold_amount * Decimal(matecoin_price)

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f)
