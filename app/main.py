import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    result_dict = {"earned_money": 0, "matecoin_account": 0}
    with open(file_name, "r") as f:
        for instance in json.load(f):
            if instance["bought"] is not None:
                result_dict[
                    "earned_money"] -= Decimal(instance[
                        "matecoin_price"]) * Decimal(instance[
                            "bought"])
                result_dict["matecoin_account"] += Decimal(instance["bought"])
            if instance["sold"] is not None:
                result_dict[
                    "earned_money"] += Decimal(instance[
                        "matecoin_price"]) * Decimal(instance["sold"])
                result_dict[
                    "matecoin_account"] -= Decimal(instance["sold"])
    result_dict["earned_money"] = str(result_dict["earned_money"])
    result_dict["matecoin_account"] = str(result_dict["matecoin_account"])

    with open("profit.json", "w") as f:
        json.dump(result_dict, f, indent=2)
