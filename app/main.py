import json

from _decimal import Decimal


def calculate_profit(name_of_the_file: str) -> None:
    temp_dict = {
        "earned_money": 0,
        "matecoin_account": 0
    }
    with open(name_of_the_file) as file:
        data_from_file = json.load(file)
    for transaction in data_from_file:
        if transaction["bought"]:
            temp_dict["matecoin_account"] += Decimal(transaction["bought"])
            temp_dict["earned_money"] -= (
                Decimal(transaction["bought"])
                * Decimal(transaction["matecoin_price"])
            )

        if transaction["sold"]:
            temp_dict["matecoin_account"] -= Decimal(transaction["sold"])
            temp_dict["earned_money"] += (
                Decimal(transaction["sold"])
                * Decimal(transaction["matecoin_price"])
            )

    result_of_day = {
        "earned_money": str(temp_dict["earned_money"]),
        "matecoin_account": str(temp_dict["matecoin_account"])
    }

    with open("profit.json", "w") as result_file:
        _ = json.dump(result_of_day, result_file, indent=2)
