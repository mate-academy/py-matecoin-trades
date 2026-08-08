# write your code here
from decimal import Decimal
import json


def calculate_profit(file_param: str) -> None:

    with open(file_param, "r") as file:
        data = json.load(file)
        bought_price = 0
        sold_price = 0
        bought = 0
        sold = 0

    for trade in data:
        if trade["bought"]:
            bought_price += Decimal(trade[
                "bought"]) * Decimal(trade["matecoin_price"])
            bought += Decimal(trade["bought"])
        if trade["sold"]:
            sold_price += Decimal(trade[
                "sold"]) * Decimal(trade["matecoin_price"])
            sold += Decimal(trade["sold"])

    profit = sold_price - bought_price
    matecoin_account = bought - sold
    with open("profit.json", "w") as profit_file:
        json.dump(
            {
                "earned_money": str(format(profit, "7f")),
                "matecoin_account": str(format(matecoin_account, "5f")),
            },
            profit_file,
            indent=2,
        )
