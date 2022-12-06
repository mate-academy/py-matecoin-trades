import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    result = {}
    balance = 0
    spend_money = 0
    earned_money = 0

    with open(file_name) as trades_info:
        converted_json_file = json.load(trades_info)

    for one_transaction in converted_json_file:

        if one_transaction["bought"] is not None:
            spend_money += Decimal(one_transaction["bought"]) * \
                Decimal(one_transaction["matecoin_price"])

            balance += Decimal(one_transaction["bought"])

        if one_transaction["sold"] is not None:
            earned_money += Decimal(one_transaction["sold"]) * \
                Decimal(one_transaction["matecoin_price"])

            balance -= Decimal(one_transaction["sold"])

    result["earned_money"] = str(earned_money - spend_money)
    result["matecoin_account"] = str(balance)

    with open("profit.json", "w") as profit_file:
        json.dump(result, profit_file, indent=2)
