import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        content = json.load(file)

    sum_of_coins = 0
    profit = 0

    for trade in content:
        if trade["bought"]:
            sum_of_coins += Decimal(trade.get("bought"))
            profit -= Decimal(
                trade.get("bought")
            ) * Decimal(
                trade.get("matecoin_price")
            )

        if trade["sold"]:
            sum_of_coins -= Decimal(trade.get("sold"))
            profit += Decimal(
                trade.get("sold")
            ) * Decimal(
                trade.get("matecoin_price")
            )

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(sum_of_coins)
    }

    with open("profit.json", "w") as new_file:
        json.dump(result, new_file, indent=2)
