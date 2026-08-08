import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades_list = json.load(f)

    earned_money = 0
    matecoin_account = 0

    for transaction in trades_list:
        rate = Decimal(transaction["matecoin_price"])
        if transaction["bought"] is not None:
            bought = Decimal(transaction["bought"])
            earned_money -= bought * rate
            matecoin_account += bought
        if transaction["sold"] is not None:
            sold = Decimal(transaction["sold"])
            earned_money += sold * rate
            matecoin_account -= sold

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
