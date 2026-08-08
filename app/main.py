from decimal import Decimal
import json


def calculate_profit(filename: str = "trades.json") -> None:
    with open(filename, "r") as file:
        trade_results = json.load(file)

    profit = {
        "earned_money": Decimal("0.0"),
        "matecoin_account": Decimal("0.0")
    }

    for deal in trade_results:
        if deal["bought"] is not None:
            do_next = Decimal(deal["bought"]) * Decimal(deal["matecoin_price"])
            profit["earned_money"] += do_next
            profit["matecoin_account"] += Decimal(deal["bought"])
        if deal["sold"] is not None:
            do_next = Decimal(deal["sold"]) * Decimal(deal["matecoin_price"])
            profit["earned_money"] -= do_next
            profit["matecoin_account"] -= Decimal(deal["sold"])

    profit["earned_money"] = str(-(profit["earned_money"]))
    profit["matecoin_account"] = str((profit["matecoin_account"]))

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
