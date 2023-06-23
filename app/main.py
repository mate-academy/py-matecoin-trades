import json
from decimal import Decimal


def calculate_profit(name_of_file: str) -> None:
    profit = 0
    mtc_acc = 0
    with open(name_of_file, "r") as file:
        data = json.load(file)
        for ma in data:
            if ma["bought"] is not None:
                mtc_acc += Decimal(ma["bought"])
                profit -= Decimal(ma["bought"]) * Decimal(ma["matecoin_price"])
            if ma["sold"] is not None:
                mtc_acc -= Decimal(ma["sold"])
                profit += Decimal(ma["sold"]) * Decimal(ma["matecoin_price"])
        with open("profit.json", "w") as out_file:
            json.dump({"earned_money": str(profit),
                       "matecoin_account": str(mtc_acc)}, out_file, indent=2)
