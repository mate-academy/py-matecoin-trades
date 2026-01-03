import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(file_name, "r") as orders:
        orders = json.load(orders)
        for order in orders:
            price = Decimal(order["matecoin_price"])
            if order["sold"] is not None:
                sold = Decimal(order["sold"])
                matecoin_account -= sold
                earned_money += sold * price
            if order["bought"] is not None:
                bought = Decimal(order["bought"])
                matecoin_account += bought
                earned_money -= bought * price
    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as orders:
        json.dump(profit, orders, indent=2)
