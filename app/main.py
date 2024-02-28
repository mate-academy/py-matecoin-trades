import json
from decimal import Decimal


def calculate_profit(file_json: str) -> None:
    result_data = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    with open(file_json) as f:
        trade_list = json.load(f)

        for one_day in trade_list:
            if one_day["bought"]:
                bought_result = Decimal(one_day["bought"]) * Decimal(one_day["matecoin_price"])
                result_data["earned_money"] -= Decimal(bought_result)
                result_data["matecoin_account"] += Decimal(one_day["bought"])

            if one_day["sold"]:
                sold_result = Decimal(one_day["sold"]) * Decimal(one_day["matecoin_price"])
                result_data["earned_money"] += sold_result
                result_data["matecoin_account"] -= Decimal(one_day["sold"])

        result_data = {
            key: str(value) for key, value in result_data.items()
        }

    with open("profit.json", "w") as f:
        json.dump(result_data, f, indent=2)
