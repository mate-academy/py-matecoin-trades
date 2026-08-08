import json
import os
from decimal import Decimal


def calculate_profit(trade_info: str) -> None:
    with open(trade_info, "r") as file:
        trades = json.load(file)

    matecoin_account = spent_money = earned_money = Decimal("0.0")

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            matecoins_bought = Decimal(trade["bought"])
            spent_money += matecoins_bought * matecoin_price
            matecoin_account += matecoins_bought

        if trade["sold"] is not None:
            matecoins_sold = Decimal(trade["sold"])
            earned_money += matecoins_sold * matecoin_price
            matecoin_account -= matecoins_sold

    profit = {
        "earned_money": str(Decimal(earned_money) - Decimal(spent_money)),
        "matecoin_account": str(matecoin_account)
    }

    profit_file_path = os.path.join(os.getcwd(), "profit.json")

    with open(profit_file_path, "w") as file:
        json.dump(profit, file, indent=2)
