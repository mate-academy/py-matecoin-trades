# write your code here
import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    result = {
        "earned_money": 0,
        "matecoin_account": 0
    }
    with (open(file_name) as f):
        trades_data = json.load(f)
        for i in trades_data:
            if i["bought"] is not None:
                result["earned_money"] -= Decimal(i["matecoin_price"]
                                                  ) * Decimal(i["bought"])
                result["matecoin_account"] += Decimal(i["bought"])
            if i["sold"] is not None:
                result["earned_money"] += Decimal(i["matecoin_price"]
                                                  ) * Decimal(i["sold"])
                result["matecoin_account"] -= Decimal(i["sold"])
        result["earned_money"] = str(result["earned_money"])
        result["matecoin_account"] = str(result["matecoin_account"])
    with open("profit.json", "w") as new_file:
        json.dump(result, new_file, indent=2)
