import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        transaction_data = json.load(f)

    profit = {
        "earned_money": decimal.Decimal("0"),
        "matecoin_account": decimal.Decimal("0")
    }

    for offer in transaction_data:
        if offer["sold"]:
            profit["matecoin_account"] -= decimal.Decimal(offer["sold"])
            profit["earned_money"] += (
                decimal.Decimal(offer["sold"])
                * decimal.Decimal(offer["matecoin_price"])
            )

        if offer["bought"]:
            profit["matecoin_account"] += decimal.Decimal(offer["bought"])
            profit["earned_money"] -= (
                decimal.Decimal(offer["bought"])
                * decimal.Decimal(offer["matecoin_price"])
            )

    profit["earned_money"] = str(profit.get("earned_money"))
    profit["matecoin_account"] = str(profit.get("matecoin_account"))

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
