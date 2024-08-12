import json
from decimal import Decimal


def calculate_profit(trades_info: str) -> None:
    with open(trades_info, "r") as file:
        trades = json.load(file)

    profit_dict = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    for trade in trades:
        if trade["bought"] is not None:
            profit_dict["earned_money"] -= (Decimal(trade["bought"])
                                            * Decimal(trade["matecoin_price"]))
            profit_dict["matecoin_account"] += Decimal(trade["bought"])

        if trade["sold"] is not None:
            profit_dict["earned_money"] += (Decimal(trade["sold"])
                                            * Decimal(trade["matecoin_price"]))
            profit_dict["matecoin_account"] -= Decimal(trade["sold"])

    profit_dict = {
        "earned_money": str(profit_dict["earned_money"]),
        "matecoin_account": str(profit_dict["matecoin_account"])
    }

    with open("profit.json", "w") as file:
        json.dump(profit_dict, file, indent=2)
