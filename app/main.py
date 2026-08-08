import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as data_file:
        data = json.load(data_file)
        coins_on_account = 0
        all_sold_value = 0
        all_bought_value = 0

    for transaction in data:
        if transaction["bought"] is not None:
            all_bought_value += Decimal(transaction["bought"]) * Decimal(
                transaction["matecoin_price"]
            )
            coins_on_account += Decimal(transaction["bought"])
        if transaction["sold"] is not None:
            all_sold_value += Decimal(transaction["sold"]) * Decimal(
                transaction["matecoin_price"]
            )
            coins_on_account -= Decimal(transaction["sold"])
    profit_dict = {
        "earned_money": str(all_sold_value - all_bought_value),
        "matecoin_account": str(coins_on_account),
    }
    with open("profit.json", "w") as result:
        json.dump(profit_dict, result, indent=2)
