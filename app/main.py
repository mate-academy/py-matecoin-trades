import json
from decimal import Decimal
import os
from pathlib import Path


def calculate_profit(json_file: str) -> None:
    base_dir = Path(__file__).resolve().parent.parent
    trades = os.path.join(base_dir, "app", json_file)
    profit = os.path.join(base_dir, "profit.json")

    with open(trades, "r") as trades_file:
        loaded_json = json.load(trades_file)

        coins = 0
        money = 0

        for item in loaded_json:
            if "bought" in item and item["bought"] is not None:
                coins += Decimal(item["bought"])
                money -= Decimal(
                    item["bought"]) * Decimal(item["matecoin_price"]
                                              )

            if "sold" in item and item["sold"] is not None:
                coins -= Decimal(item["sold"])
                money += Decimal(
                    item["sold"]) * Decimal(item["matecoin_price"]
                                            )

        dict_to_dump = {
            "earned_money": str(money),
            "matecoin_account": str(coins)
        }

        with open(profit, "w") as profit_file:
            json.dump(dict_to_dump, profit_file, indent=2)
