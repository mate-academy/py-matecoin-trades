import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    result = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    with open(name_file, "r") as file:
        trades_information = json.load(file)

        for transaction in trades_information:
            check_count_coin = (
                (
                    (Decimal(transaction["bought"])
                     if transaction["bought"] is not None
                     else 0)
                )
                - (
                    (Decimal(transaction["sold"])
                     if transaction["sold"] is not None
                     else 0)
                )
            )
            result["earned_money"] -= (
                check_count_coin
                * (Decimal(transaction["matecoin_price"]))
            )
            result["matecoin_account"] += check_count_coin

    result = {
        "earned_money": str(result["earned_money"]),
        "matecoin_account": str(result["matecoin_account"])
    }

    with open("../profit.json", "w") as new_file:
        json.dump(result, new_file, indent=2)
