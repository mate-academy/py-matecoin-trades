import json

from decimal import Decimal


def calculate_profit(name: str) -> None:
    with open(name, "r") as f:
        trade_data = json.load(f)

    earned_money = 0
    matecoin_account = 0

    for deal in trade_data:
        bought = deal["bought"]
        sold = deal["sold"]
        matecoin_price = Decimal(deal["matecoin_price"])

        if sold:
            earned_money += matecoin_price * Decimal(sold)
            matecoin_account -= Decimal(sold)

        if bought:
            earned_money -= matecoin_price * Decimal(bought)
            matecoin_account += Decimal(bought)

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
