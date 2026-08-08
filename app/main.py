from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    result = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }
    with (open(f"{file_name}", "r") as file_in,
          open("profit.json", "w") as profit):

        for data in json.load(file_in):
            matecoin_price = Decimal(data["matecoin_price"])
            if data["bought"]:
                bought = Decimal(data["bought"])
                result["earned_money"] -= bought * matecoin_price
                result["matecoin_account"] += Decimal(bought)
            if data["sold"]:
                sold = Decimal(data["sold"])
                result["earned_money"] += sold * matecoin_price
                result["matecoin_account"] -= sold

        result["earned_money"] = str(result["earned_money"])
        result["matecoin_account"] = str(result["matecoin_account"])

        json.dump(result, profit, indent=2)
