import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as input_file:
        coin_data = json.load(input_file)

        money_earned = 0
        account = 0

        for operation in coin_data:
            price = Decimal(operation["matecoin_price"])

            if operation["bought"]:
                account += Decimal(operation["bought"])
                money_earned -= Decimal(operation["bought"]) * price

            if operation["sold"]:
                account -= Decimal(operation["sold"])
                money_earned += Decimal(operation["sold"]) * price

            output_json = {
                "earned_money": str(money_earned),
                "matecoin_account": str(account)
            }

            with open("profit.json", "w") as output_file:
                json.dump(output_json, output_file, indent=2)
