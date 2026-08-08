import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    money_profit = 0
    current_coin_account = 0

    with open(file_name, "r") as file:
        trades_list = json.load(file)

    for trade in trades_list:
        if trade["bought"]:
            money_profit -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
            current_coin_account += Decimal(trade["bought"])
        if trade["sold"]:
            money_profit += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))
            current_coin_account -= Decimal(trade["sold"])

    result_dictionary = {
        "earned_money": str(money_profit),
        "matecoin_account": str(current_coin_account)
    }

    with open("profit.json", "w") as result_file:
        json.dump(result_dictionary, result_file, indent=2)
