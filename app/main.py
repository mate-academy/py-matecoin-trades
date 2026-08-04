import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    trades = []
    with open(file_name) as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            earned_money -= Decimal(trade["bought"]) * price
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"] is not None:
            earned_money += Decimal(trade["sold"]) * price
            matecoin_account -= Decimal(trade["sold"])

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as save_file:
        json.dump(profit, save_file, indent=2)
