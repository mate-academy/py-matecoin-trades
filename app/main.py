import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    result_dict = {"earned_money": 0, "matecoin_account": 0}
    with open(file_name, "r") as file_json:
        text_py = json.load(file_json)
    for operation in text_py:
        bought = Decimal(operation["bought"] or 0)
        sold = Decimal(operation["sold"] or 0)
        prise = Decimal(operation["matecoin_price"])
        result_dict["matecoin_account"] += bought - sold
        result_dict["earned_money"] += (-(bought * prise)
                                        + (sold * prise))
        # Decimal(float(operation["bought"]), 5)
    result_dict["matecoin_account"] = str(result_dict["matecoin_account"])
    result_dict["earned_money"] = str(result_dict["earned_money"])
    # data_to_json = json.dumps(result_dict)
    with open("profit.json", "w") as f:
        json.dump(result_dict, f, indent=2)
        # f.write(data_to_json)

    # print(result_dict)


# calculate_profit("trades.json")
