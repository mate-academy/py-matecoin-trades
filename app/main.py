import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    result = {
        "earned_money": "0",
        "matecoin_account": "0"
    }

    with open(filename, "r") as filename:
        trades = json.load(filename)

    for contract in trades:
        if contract["bought"]:
            result["matecoin_account"] = str(
                Decimal(result["matecoin_account"])
                + Decimal(contract["bought"])
            )
            result["earned_money"] = str(
                Decimal(result["earned_money"])
                - Decimal(contract["bought"])
                * Decimal(contract["matecoin_price"])
            )

        if contract["sold"]:
            result["matecoin_account"] = str(
                Decimal(result["matecoin_account"])
                - Decimal(contract["sold"])
            )
            result["earned_money"] = str(
                Decimal(result["earned_money"])
                + Decimal(contract["sold"])
                * Decimal(contract["matecoin_price"])
            )

    with open("profit.json", "w") as filename:
        json.dump(result, filename, indent=2)
