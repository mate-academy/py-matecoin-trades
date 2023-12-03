import json
from decimal import Decimal


def calculate_profit(json_file: str) -> None:
    profit = {
        "earned_money" : 0,
        "matecoin_account" : 0
    }

    with open(json_file, "r") as trades_result_json:
        trades_result = json.load(trades_result_json)
    for cryptocoin in trades_result:
        if cryptocoin["bought"]:
            print(type(cryptocoin["bought"]))
            bought = Decimal(cryptocoin["bought"])
            profit["earned_money"] -=\
                bought * Decimal(cryptocoin["matecoin_price"])
            profit["matecoin_account"] += bought
        if cryptocoin["sold"]:
            sold = Decimal(cryptocoin["sold"])
            profit["earned_money"] +=\
                sold * Decimal(cryptocoin["matecoin_price"])
            profit["matecoin_account"] -= sold

    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])

    with open("profit.json", "w") as profit_file_json:
        json.dump(profit, profit_file_json, indent=2)
