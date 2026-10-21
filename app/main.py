from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as f:
        trades = json.load(f)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        price = Decimal(trade["matecoin_price"])

        if bought is not None:
            bought_vol = Decimal(bought)
            earned_money -= bought_vol * price
            matecoin_account += bought_vol

        if sold is not None:
            sold_vol = Decimal(sold)
            earned_money += sold_vol * price
            matecoin_account -= sold_vol

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)
