import json
from decimal import Decimal


def calculate_profit(json_file: str) -> None:
    result_dict = \
        {
            "earned_money": Decimal(0),
            "matecoin_account": Decimal(0)
        }
    with open(json_file, "r") as information:
        info_with_json = json.load(information)
    for item in info_with_json:
        if item["bought"] is not None:
            matecoin_item = Decimal(item["matecoin_price"])
            bought_item = Decimal(item["bought"])
            result_dict["earned_money"] -= bought_item * matecoin_item
            result_dict["matecoin_account"] += Decimal(item["bought"])
        if item["sold"] is not None:
            matecoin_item = Decimal(item["matecoin_price"])
            sold_item = Decimal(item["sold"])
            result_dict["earned_money"] += sold_item * matecoin_item
            result_dict["matecoin_account"] -= Decimal(item["sold"])
    result_dict["earned_money"] = str(result_dict["earned_money"])
    result_dict["matecoin_account"] = str(result_dict["matecoin_account"])

    with open("profit.json", "w") as new_file:
        json.dump(result_dict, new_file, indent=2)
