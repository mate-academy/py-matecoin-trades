import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        in_list = json.load(file)

    out_dict = {
        "earned_money": decimal.Decimal(0),
        "matecoin_account": decimal.Decimal(0)
    }
    for value in in_list:
        matecoin_price = decimal.Decimal(value["matecoin_price"])
        if value["bought"] is not None:
            bought = decimal.Decimal(value["bought"])
            out_dict["earned_money"] -= bought * matecoin_price
            out_dict["matecoin_account"] += bought
        if value["sold"] is not None:
            sold = decimal.Decimal(value["sold"])
            out_dict["earned_money"] += sold * matecoin_price
            out_dict["matecoin_account"] -= sold
    out_dict["earned_money"] = str(out_dict["earned_money"])
    out_dict["matecoin_account"] = str(out_dict["matecoin_account"])

    with open("profit.json", "w") as file:
        json.dump(out_dict, file, indent=2)
