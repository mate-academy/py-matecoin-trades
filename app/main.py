import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    """Calculate profit and remaining Matecoin balance."""
    with open(filename, "r", encoding="utf-8") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        price = Decimal(trade["matecoin_price"])

        if bought:
            bought_amount = Decimal(bought)
            earned_money -= bought_amount * price
            matecoin_account += bought_amount

        if sold:
            sold_amount = Decimal(sold)
            earned_money += sold_amount * price
            matecoin_account -= sold_amount

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w", encoding="utf-8") as file:
        json.dump(profit_data, file, ensure_ascii=False, indent=2)
