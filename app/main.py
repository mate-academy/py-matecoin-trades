import json
from decimal import Decimal


def calculate_profit(file_json: str) -> None:
    with open(file_json) as file:
        trades = json.load(file)

        earned_money = Decimal("0")
        matecoin_account = Decimal("0")

        for operation in trades:

            matecoin_price = Decimal(operation["matecoin_price"])

            if operation["bought"] is not None:
                bought = Decimal(operation["bought"])

                earned_money -= bought * matecoin_price
                matecoin_account += bought
            if operation["sold"] is not None:
                sold = Decimal(operation["sold"])

                earned_money += sold * matecoin_price
                matecoin_account -= sold

    with open("profit.json", "w") as file:
        finally_dict = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        json.dump(finally_dict, file, indent=2)
