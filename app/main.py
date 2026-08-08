import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    result = {"bought": 0, "sold": 0, "amount": 0}
    with open(file_name, "r") as source, open("profit.json", "w") as file_to:
        new_file = json.load(source)
        for data in new_file:
            if data["bought"]:
                result["bought"] += (Decimal(data["bought"])
                                     * Decimal(data["matecoin_price"]))
                result["amount"] += Decimal(data["bought"])
            if data["sold"]:
                result["sold"] += (Decimal(data["sold"])
                                   * Decimal(data["matecoin_price"]))
                result["amount"] -= Decimal(data["sold"])
        result = {
            "earned_money": str(result["sold"] - result["bought"]),
            "matecoin_account": str(result["amount"])
        }
        json.dump(result, file_to, indent=2)
