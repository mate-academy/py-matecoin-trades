import json
from decimal import Decimal


def calculate_profit(document) -> None:
    with open(document, "r") as file:
        currency = json.load(file)



    result = {
        "matecoin_account": Decimal("0"),
        "earned_money": Decimal("0")
    }

    for entry in currency:
        price = Decimal(entry["matecoin_price"])

        if entry["bought"] is not None:
            bought_amount = Decimal(entry["bought"])
            result["matecoin_account"] += bought_amount
            result["earned_money"] -= bought_amount * price

        if entry["sold"] is not None:
            sold_amount = Decimal(entry["sold"])
            result["matecoin_account"] -= sold_amount
            result["earned_money"] += sold_amount * price

    with open("profit.json", "w") as result_file:
        json.dump(
            {
                "matecoin_account": str(result["matecoin_account"]),
                "earned_money": str(result["earned_money"])
            },
            result_file
        )
