import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    total_spent = Decimal("0")
    total_earned = Decimal("0")
    matecoin_account = Decimal("0")

    with open(trades_file, "r") as file:
        trades = json.load(file)

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        price = Decimal(trade.get("matecoin_price"))

        if bought is not None:
            bought_amount = Decimal(bought)
            matecoin_account += bought_amount
            total_spent += bought_amount * price

        if sold is not None:
            sold_amount = Decimal(sold)
            matecoin_account -= sold_amount
            total_earned += sold_amount * price

    earned_money = total_earned - total_spent

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as outfile:
        json.dump(profit_data, outfile, indent=4)


calculate_profit("trades.json")
