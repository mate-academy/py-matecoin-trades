import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    with (open(file_path, "r") as input_file,
          open("profit.json", "w") as output_file):
        data = json.load(input_file)

        earned_money = Decimal("0.0")
        matecoin_account = Decimal("0.0")

        for operation in data:
            if operation.get("bought"):
                earned_money -= Decimal(
                    Decimal(operation.get("matecoin_price"))
                    * Decimal(operation.get("bought"))
                )
                matecoin_account += Decimal(operation.get("bought"))

            if operation.get("sold"):
                earned_money += Decimal(
                    Decimal(operation.get("matecoin_price"))
                    * Decimal(operation.get("sold"))
                )
                matecoin_account -= Decimal(operation.get("sold"))

        calculated_profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account),
        }

        json.dump(calculated_profit, output_file, indent=2)
