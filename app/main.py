import json
from decimal import Decimal


def calculate_profit(document: str) -> None:
    with open(document, "r") as file:
        currency = json.load(file)

    result = {
        "matecoin_account": Decimal("0"),
        "earned_money": Decimal("0")
    }

    for entry in currency:
        price = Decimal(entry["matecoin_price"])

        if entry["bought"] is not None:
            result["matecoin_account"] += Decimal(entry["bought"])
            result["earned_money"] -= (Decimal(entry["bought"]) * price)

        if entry["sold"] is not None:
            result["matecoin_account"] -= Decimal(entry["sold"])
            result["earned_money"] += (Decimal(entry["sold"]) * price)

    with open("profit.json", "w") as result_file:
        json.dump(
            {
                "earned_money": str(result["earned_money"]),
                "matecoin_account": str(result["matecoin_account"]),

            },
            result_file,
            indent=2)
