import json
from decimal import Decimal


def calculate_profit(way_to_file: str) -> None:
    profit_data = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }
    with open(way_to_file) as trades_file:
        trades_data = json.load(trades_file)
        for el in trades_data:
            if el["bought"] is not None:
                profit_data["earned_money"] -= (
                    Decimal(el["bought"]) * Decimal(el["matecoin_price"])
                )
                profit_data["matecoin_account"] += Decimal(el["bought"])
            if el["sold"] is not None:
                profit_data["earned_money"] += (
                    Decimal(el["sold"]) * Decimal(el["matecoin_price"])
                )
                profit_data["matecoin_account"] -= Decimal(el["sold"])

    result_data = {
        "earned_money": str(profit_data["earned_money"]),
        "matecoin_account": str(profit_data["matecoin_account"])
    }
    with open("profit.json", "w") as profit_file:
        json.dump(result_data, profit_file, indent=2)
