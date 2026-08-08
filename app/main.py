import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)

    total_earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    # Process each trade
    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = Decimal(trade.get("matecoin_price"))

        if bought is not None:
            bought_amount = Decimal(bought)
            matecoin_account += bought_amount
        elif sold is not None:
            sold_amount = Decimal(sold)
            matecoin_account -= sold_amount
            total_earned_money += sold_amount * matecoin_price

    total_spent_money = sum(
        (Decimal(trade["bought"]) * Decimal(trade["matecoin_price"]))
        for trade in trades if trade.get("bought") is not None
    )

    total_earned_money -= total_spent_money

    result = {
        "earned_money": str(total_earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file)


calculate_profit("trades.json")
