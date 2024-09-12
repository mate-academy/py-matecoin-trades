import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as trades_file:
        trades = json.load(trades_file)

    result_dict = {"earned_money": decimal.Decimal("0"),
                   "matecoin_account": decimal.Decimal("0")}

    for trade in trades:
        price = decimal.Decimal(trade["matecoin_price"])

        if trade["bought"]:
            bought = decimal.Decimal(trade["bought"])
            result_dict["earned_money"] -= bought * price
            result_dict["matecoin_account"] += bought

        if trade["sold"]:
            sold = decimal.Decimal(trade["sold"])
            result_dict["earned_money"] += sold * price
            result_dict["matecoin_account"] -= sold

    result_dict["earned_money"] = str(result_dict["earned_money"])
    result_dict["matecoin_account"] = str(result_dict["matecoin_account"])

    with open("profit.json", "w") as result_file:
        json.dump(result_dict, result_file, indent=2)
