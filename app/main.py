import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    with open(file_path, "r") as file:
        data = json.load(file)

        result = {"earned_money": 0, "matecoin_account": 0}

        for operation in data:
            price = Decimal(operation["matecoin_price"])

            if operation["bought"] is not None:
                bought = Decimal(operation["bought"])
                result["earned_money"] -= bought * price
                result["matecoin_account"] += bought

            if operation["sold"] is not None:
                sold = Decimal(operation["sold"])
                result["earned_money"] += sold * price
                result["matecoin_account"] -= sold

        with open("profit.json", "w") as profit_file:
            result["earned_money"] = str(result["earned_money"])
            result["matecoin_account"] = str(result["matecoin_account"])
            json.dump(result, profit_file, indent=2)
