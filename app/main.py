import json
from decimal import Decimal


def calculate_profit(json_trade_info: str) -> None:
    with open(json_trade_info, "r") as file:
        trades = json.load(file)
        earned_money = Decimal("0")
        matecoin_account = Decimal("0")

        for trade in trades:
            if trade["bought"] is not None:
                bought = Decimal(trade["bought"])
                price = Decimal(trade["matecoin_price"])
                earned_money -= bought * price
                matecoin_account += bought

            if trade["sold"] is not None:
                sold = Decimal(trade["sold"])
                price = Decimal(trade["matecoin_price"])
                earned_money += sold * price
                matecoin_account -= sold

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
