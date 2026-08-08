import decimal
import json


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        transactions = json.load(file)

    profit_dict = {
        "earned_money": 0,
        "matecoin_account": 0
    }
    for trans in transactions:
        if trans["bought"] and trans["sold"]:
            profit_dict["earned_money"] -= (
                decimal.Decimal(trans["bought"])
                * decimal.Decimal(trans["matecoin_price"])
            )
            profit_dict["matecoin_account"] += decimal.Decimal(trans["bought"])
            profit_dict["earned_money"] += (
                decimal.Decimal(trans["sold"])
                * decimal.Decimal(trans["matecoin_price"])
            )
            profit_dict["matecoin_account"] -= decimal.Decimal(trans["sold"])
        elif trans["bought"] and not trans["sold"]:
            profit_dict["earned_money"] -= (
                decimal.Decimal(trans["bought"])
                * decimal.Decimal(trans["matecoin_price"])
            )
            profit_dict["matecoin_account"] += decimal.Decimal(trans["bought"])
        elif not trans["bought"] and trans["sold"]:
            profit_dict["earned_money"] += (
                decimal.Decimal(trans["sold"])
                * decimal.Decimal(trans["matecoin_price"])
            )
            profit_dict["matecoin_account"] -= decimal.Decimal(trans["sold"])

    for key in profit_dict:
        profit_dict[key] = str(profit_dict[key])

    with open("profit.json", "w") as file:
        json.dump(profit_dict, file, indent=2)
