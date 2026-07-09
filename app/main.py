import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    with open(trades, "r") as file:
        transaction_info = json.load(file)
    result_dict = {}
    earned_money = 0
    coins_amount = 0
    for transaction in transaction_info:
        if transaction["sold"] is not None:
            earned_money += (Decimal(transaction["sold"])
                             * Decimal(transaction["matecoin_price"]))
            coins_amount -= Decimal(transaction["sold"])
        if transaction["bought"] is not None:
            earned_money -= (Decimal(transaction["bought"])
                             * Decimal(transaction["matecoin_price"]))
            coins_amount += Decimal(transaction["bought"])

    result_dict["earned_money"] = str(earned_money)
    result_dict["matecoin_account"] = str(coins_amount)

    with open("profit.json", "w") as result_file:
        json.dump(result_dict, result_file, indent=2)
