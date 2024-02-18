import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    result = {
        "earned_money": 0,
        "matecoin_account": 0
    }
    with (open(filename, "r") as f):
        datas = json.load(f)
        for ln in datas:
            if ln["bought"]:
                bought = Decimal(ln["bought"]) * Decimal(ln["matecoin_price"])
                result["earned_money"] -= Decimal(bought)
                result["matecoin_account"] += Decimal(ln["bought"])
            if ln["sold"]:
                sold = Decimal(ln["sold"]) * Decimal(ln["matecoin_price"])
                result["earned_money"] += sold
                result["matecoin_account"] -= Decimal(ln["sold"])

    result = {key: str(value) for key, value in result.items()}
    with open("profit.json", "w") as fw:
        json.dump(result, fw, indent=2)
