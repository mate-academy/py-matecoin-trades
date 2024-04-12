from decimal import Decimal
import json


def calculate_profit(file_json: json) -> None:
    total_income = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    def check_bought(action: dict) -> None:
        total_income["earned_money"] -= (
            Decimal(action["matecoin_price"])
            * Decimal(action["bought"]))
        total_income["matecoin_account"] += Decimal(action["bought"])

    def check_sold(action: dict) -> None:
        total_income["earned_money"] += (
            Decimal(action["matecoin_price"])
            * Decimal(action["sold"]))
        total_income["matecoin_account"] -= Decimal(action["sold"])

    with open(file_json, "r") as json_file:
        for transaction in json.load(json_file):
            if transaction["bought"] is None:
                check_sold(transaction)
            elif transaction["bought"] and transaction["sold"]:
                check_sold(transaction)
                check_bought(transaction)
            else:
                check_bought(transaction)

    total_income["earned_money"] = (
        str(total_income.get("earned_money")))
    total_income["matecoin_account"] = (
        str(total_income.get("matecoin_account")))

    with open("profit.json", "w") as json_file:
        json.dump(total_income, json_file, indent=2)
