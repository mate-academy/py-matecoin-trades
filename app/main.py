import json
from decimal import Decimal


def calculate_profit(trades_data: str) -> None:
    with open("app/trades.json", "r") as file:
        trades_data = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades_data:
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought_value = Decimal(trade["bought"])
            cost = bought_value * matecoin_price
            matecoin_account += bought_value
            earned_money -= cost

        if trade["sold"] is not None:
            sold_value = Decimal(trade["sold"])
            revenue = sold_value * matecoin_price
            matecoin_account -= sold_value
            earned_money += revenue

        earned_money_str = str(earned_money)
        matecoin_account_str = str(matecoin_account)

        result_dict = {
            "earned_money": earned_money_str,
            "matecoin_account": matecoin_account_str
        }

        with open("profit.json", "w") as result_file:
            json.dump(result_dict, result_file, indent=2)
