import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(f"{file_name}") as f:
        trade_operations = json.load(f)
    prof = {"earned_money": Decimal("0.0"),
            "matecoin_account": Decimal("0.0")}
    for op in trade_operations:
        if op.get("bought"):
            prof["earned_money"] -= (Decimal(op["bought"])
                                     * Decimal(op["matecoin_price"]))
            prof["matecoin_account"] += Decimal(op["bought"])
        if op.get("sold"):
            prof["earned_money"] += (Decimal(op["sold"])
                                     * Decimal(op["matecoin_price"]))
            prof["matecoin_account"] -= Decimal(op["sold"])
    prof["earned_money"] = str(prof.get("earned_money"))
    prof["matecoin_account"] = str(prof.get("matecoin_account"))
    with open("profit.json", "w") as f:
        json.dump(prof, f, indent=2)
