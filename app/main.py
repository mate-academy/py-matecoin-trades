import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    matecoin_account = Decimal("0.0")
    earned_money = Decimal("0.0")
    with open(file_name, "r") as file:
        data = json.load(file)
        for day_data in data:
            if day_data["sold"] is None:
                matecoin_account += Decimal(day_data["bought"])
                earned_money -= Decimal(day_data["matecoin_price"]) * Decimal(
                    day_data["bought"]
                )
            if day_data["bought"] is None:
                matecoin_account -= Decimal(day_data["sold"])
                earned_money += Decimal(day_data["matecoin_price"]) * Decimal(
                    day_data["sold"]
                )
            if day_data["sold"] and day_data["bought"]:
                matecoin_account += Decimal(day_data["bought"])
                earned_money -= Decimal(day_data["matecoin_price"]) * Decimal(
                    day_data["bought"]
                )
                matecoin_account -= Decimal(day_data["sold"])
                earned_money += Decimal(day_data["matecoin_price"]) * Decimal(
                    day_data["sold"]
                )

    result_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as f:
        json.dump(result_dict, f, indent=2)
