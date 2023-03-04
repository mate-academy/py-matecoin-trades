import json
from decimal import Decimal
from typing import NewType

JsonType = NewType("JsonType", json)


def calculate_profit(json_file: JsonType) -> JsonType:
    with open(json_file, "r") as f:
        storage = json.load(f)
    total_mate_coin = sum(
        [Decimal(wallet["bought"])
         for wallet in storage if wallet["bought"] is not None]
    ) - sum(
        [Decimal(wallet["sold"])
         for wallet in storage if wallet["sold"] is not None]
    )
    total_dollar = sum(
        [Decimal(wallet["sold"]) * Decimal(wallet["matecoin_price"])
         for wallet in storage if wallet["sold"] is not None]
    ) - sum(
        [Decimal(wallet["bought"]) * Decimal(wallet["matecoin_price"])
         for wallet in storage if wallet["bought"] is not None]
    )
    result_dict = {
        "earned_money": total_dollar.__str__(),
        "matecoin_account": total_mate_coin.__str__()
    }
    with open("profit.json", "w") as json_file:
        json.dump(result_dict, json_file, indent=2)
