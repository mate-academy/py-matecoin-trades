import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    result = {"earned_money": Decimal("0"),
              "matecoin_account": Decimal("0")}

    with (open(file_name, "r") as file,
          open("profit.json", "w") as end_result):
        data = json.load(file)
        for transaction in data:

            if transaction["sold"] is not None:
                result["earned_money"] += (
                        Decimal(transaction["sold"])
                        * Decimal(transaction["matecoin_price"])
                )
                result["matecoin_account"] -= Decimal(transaction["sold"])

            if transaction["bought"] is not None:

                result["matecoin_account"] += Decimal(transaction["bought"])
                result["earned_money"] -= (
                        Decimal(transaction["bought"])
                        * Decimal(transaction["matecoin_price"])
                )
        result["earned_money"] = str(result["earned_money"])
        result["matecoin_account"] = str(result["matecoin_account"])
        json.dump(result, end_result, indent=2)
