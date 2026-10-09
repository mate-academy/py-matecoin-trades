import json

from decimal import Decimal


def calculate_profit(data_file_name: str) -> None:
    trade_res = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    with open(data_file_name, "r") as file:
        current_data = json.load(file)

    for trade in current_data:
        if trade["bought"]:
            trade_res["earned_money"] = (trade_res["earned_money"]
                                         - Decimal(trade["bought"])
                                         * Decimal(trade["matecoin_price"]))
            trade_res["matecoin_account"] = (trade_res["matecoin_account"]
                                             + Decimal(trade["bought"]))

        if trade["sold"]:
            trade_res["earned_money"] = (trade_res["earned_money"]
                                         + Decimal(trade["sold"])
                                         * Decimal(trade["matecoin_price"]))
            trade_res["matecoin_account"] = (trade_res["matecoin_account"]
                                             - Decimal(trade["sold"]))

    refactored_data = {k: str(v) for k, v in trade_res.items()}

    with open("profit.json", "w") as file:
        json.dump(refactored_data, file, indent=2)
