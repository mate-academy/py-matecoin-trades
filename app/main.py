import json
from decimal import Decimal


def calculate_profit(json_file: str) -> None:
    result = {
        "earned_money": None,
        "matecoin_account": None
    }
    bought = Decimal(0)
    sold = Decimal(0)
    coin = Decimal(0)
    with open(json_file, "r") as f:
        info_list = json.load(f)

        for trade in info_list:
            if trade["bought"] is not None:
                bought += (Decimal(trade["bought"])
                           * Decimal(trade["matecoin_price"]))
                coin += Decimal(trade["bought"])
            if trade["sold"] is not None:
                sold += (Decimal(trade["sold"])
                         * Decimal(trade["matecoin_price"]))
                coin -= Decimal(trade["sold"])
    result["earned_money"] = f"{sold - bought}"
    result["matecoin_account"] = f"{coin}"
    with open("profit.json", "w") as profit:
        json.dump(result, profit, indent=2)
