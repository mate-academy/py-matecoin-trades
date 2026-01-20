import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        info_file = json.load(f)
    accounts = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")}
    for info in info_file:
        if info.get("bought") is not None:
            accounts["earned_money"] -= (
                Decimal(info["bought"]) * Decimal(info["matecoin_price"])
            )
            accounts["matecoin_account"] += Decimal(info["bought"])
        if info.get("sold") is not None:
            accounts["matecoin_account"] -= Decimal(info["sold"])
            accounts["earned_money"] += (
                Decimal(info["sold"]) * Decimal(info["matecoin_price"])
            )
    accounts["earned_money"] = str(accounts["earned_money"])
    accounts["matecoin_account"] = str(accounts["matecoin_account"])
    with open("profit.json", "w") as f:
        json.dump(accounts, f, indent=2)
