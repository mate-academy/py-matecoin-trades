import json

import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades_from_file = json.load(f)
    res_earned_money = 0
    res_matecoin_account = 0
    for symbol in trades_from_file:
        if symbol["bought"] is not None:
            res_earned_money -= decimal.Decimal(symbol["bought"]) * decimal.Decimal(symbol["matecoin_price"])
            res_matecoin_account += decimal.Decimal(symbol["bought"])
        if symbol["sold"] is not None:
            res_earned_money += decimal.Decimal(symbol["sold"]) * decimal.Decimal(symbol["matecoin_price"])
            res_matecoin_account -= decimal.Decimal(symbol["sold"])
    dict_of_results = {
  "earned_money": str(res_earned_money),
  "matecoin_account": str(res_matecoin_account)
}

    with open("profit.json", "w") as new_file:
        json.dump(dict_of_results, new_file, indent=2)
