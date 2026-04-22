from decimal import Decimal
import json


def calculate_profit(name: str) -> None:
    with open(name, "r") as file:
        trades = json.load(file)

    matecoin_account = Decimal("0")
    total_bought, total_sold = Decimal("0"), Decimal("0")
    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])
        if trade.get("bought"):
            matecoin_account += Decimal(trade["bought"])
            total_bought += Decimal(trade["bought"]) * matecoin_price
        if trade.get("sold"):
            matecoin_account -= Decimal(trade["sold"])
            total_sold += Decimal(trade["sold"]) * matecoin_price

    earned_money = total_sold - total_bought
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
