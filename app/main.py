import json
from decimal import Decimal


def calculate_profit(name_of_json_file: str) -> None:
    bought_amount = 0
    sold_amount = 0
    profit = 0
    coin_account = 0

    with open(f"{name_of_json_file}") as file:
        trades = json.load(file)

    for trade in trades:
        if trade["bought"] is not None:
            coin_account += Decimal(trade["bought"])
            bought_amount += (
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )

        if trade["sold"] is not None:
            coin_account -= Decimal(trade["sold"])
            sold_amount += (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )

    profit = sold_amount - bought_amount

    result_string = {
        "earned_money": str(profit),
        "matecoin_account": str(coin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(result_string, file, indent=2)
