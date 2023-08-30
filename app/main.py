import json
from decimal import Decimal


def calculate_profit(trade_information_file: str) -> None:
    earned_money = 0
    matecoin_account = 0

    with open(trade_information_file, "r") as info_file:

        trades_info = json.load(info_file)

        for trade in trades_info:
            if trade["bought"] is not None:

                bought = Decimal(trade["bought"])
                matecoin_price = Decimal(trade["matecoin_price"])

                earned_money -= bought * matecoin_price
                matecoin_account += bought

            if trade["sold"] is not None:

                sold = Decimal(trade["sold"])
                matecoin_price = Decimal(trade["matecoin_price"])

                earned_money += sold * matecoin_price
                matecoin_account -= sold

    with open("profit.json", "w") as profit_file:

        content = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }
        json.dump(content, profit_file, indent=2)
