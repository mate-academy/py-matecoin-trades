import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    total = 0
    total_money = 0
    with open(file_name, "r") as file:
        data = json.load(file)

        for value in data:
            if value["bought"] is not None:
                bought = Decimal(value["bought"])
                total += bought
                total_money -= bought * Decimal(value["matecoin_price"])

            if value["sold"] is not None:
                sold = Decimal(value["sold"])
                total -= sold
                total_money += sold * Decimal(value["matecoin_price"])

    result_dict = {"earned_money": total_money, "matecoin_account": total}
    result_dict["earned_money"] = str(result_dict["earned_money"])
    result_dict["matecoin_account"] = str(result_dict["matecoin_account"])

    with open("profit.json", "w") as f:
        json.dump(result_dict, f, indent=2)
