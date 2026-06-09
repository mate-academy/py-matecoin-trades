from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])

        bought_str = trade["bought"]
        sold_str = trade["sold"]
        if bought_str is not None:
            earned_money -= Decimal(bought_str) * matecoin_price
            matecoin_account += Decimal(bought_str)
        if sold_str is not None:
            earned_money += Decimal(sold_str) * matecoin_price
            matecoin_account -= Decimal(sold_str)

    with open("profit.json", "w") as file:
        json.dump({
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }, file, indent=2)
