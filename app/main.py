import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as f:
        input_list = json.load(f)
    output_dict = {
        "earned_money": 0,
        "matecoin_account": 0
    }
    for day in input_list:
        for _ in day.items():
            if day["sold"] is None:
                day["sold"] = 0
            if day["bought"] is None:
                day["bought"] = 0

            bought = Decimal(day["bought"])
            sold = Decimal(day["sold"])
            price = Decimal(day["matecoin_price"])

            output_dict["earned_money"] += ((sold - bought) * price)
            output_dict["matecoin_account"] += (bought - sold)

    output_dict["earned_money"] = str(output_dict["earned_money"])
    output_dict["matecoin_account"] = str(output_dict["matecoin_account"])

    with open("profit.json", "w") as f:
        json.dump(output_dict, f)


calculate_profit("trades.json")
