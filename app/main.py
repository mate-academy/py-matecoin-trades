import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        json_file = json.load(file)
    bought = 0
    sold = 0
    profit = {}
    for tran in json_file:
        if tran.get("bought"):
            bought += Decimal(tran["bought"]) * Decimal(tran["matecoin_price"])
            matecoin = Decimal(profit.get("matecoin_account", 0))
            profit["matecoin_account"] = matecoin + Decimal(tran["bought"])
        if tran.get("sold"):
            sold += Decimal(tran["sold"]) * Decimal(tran["matecoin_price"])
            matecoin = Decimal(profit.get("matecoin_account", 0))
            profit["matecoin_account"] = matecoin - Decimal(tran["sold"])
    result = {
        "earned_money": str(sold - bought),
        "matecoin_account": str(profit["matecoin_account"])
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
