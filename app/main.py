import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    profit = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0"),
    }
    if name is not None:
        with open(name, "r") as json_data:
            data = json.load(json_data)
            for i in data:
                if i["bought"] is not None and i["sold"] is None:
                    profit["matecoin_account"] += Decimal(i["bought"])
                    profit["earned_money"] -= Decimal(
                        i["bought"]) * Decimal(i["matecoin_price"])
                elif i["bought"] is None and i["sold"] is not None:
                    profit["matecoin_account"] -= Decimal(i["sold"])
                    profit["earned_money"] += Decimal(
                        i["sold"]) * Decimal(i["matecoin_price"])
                else:
                    profit["matecoin_account"] -= Decimal(i["sold"])
                    profit["earned_money"] += Decimal(
                        i["sold"]) * Decimal(i["matecoin_price"])
                    profit["matecoin_account"] += Decimal(i["bought"])
                    profit["earned_money"] -= Decimal(
                        i["bought"]) * Decimal(i["matecoin_price"])
    profit["earned_money"] = str(profit["earned_money"])
    profit["matecoin_account"] = str(profit["matecoin_account"])
    with open("profit.json", "w") as json_file:
        json.dump(profit, json_file, indent=2)
