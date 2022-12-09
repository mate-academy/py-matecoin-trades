import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r", encoding="utf-8") as file_in:
        trade_data = json.load(file_in)
    result_data = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    for trade in trade_data:
        try:
            result_data["earned_money"] -= \
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            result_data["matecoin_account"] += Decimal(trade["bought"])
        except TypeError:
            pass
        try:
            result_data["earned_money"] += \
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            result_data["matecoin_account"] -= Decimal(trade["sold"])
        except TypeError:
            pass

    result_data["earned_money"] = str(result_data["earned_money"])
    result_data["matecoin_account"] = str(result_data["matecoin_account"])

    with open("profit.json", "w", encoding="utf-8") as file_out:
        json.dump(result_data, file_out, indent=2)
