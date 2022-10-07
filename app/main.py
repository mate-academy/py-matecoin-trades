import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades_info = json.load(file)

    bought_dollars, sold_dollars, bought_matecoin, sold_matecoin = (0, 0, 0, 0)

    for info in trades_info:
        bought_dollars += (Decimal((info["bought"], 0)[not info["bought"]])
                           * Decimal(info["matecoin_price"]))
        sold_dollars += (Decimal((info["sold"], 0)[not info["sold"]])
                         * Decimal(info["matecoin_price"]))
        bought_matecoin += Decimal((info["bought"], 0)[not info["bought"]])
        sold_matecoin += Decimal((info["sold"], 0)[not info["sold"]])

    profit = {
        "earned_money": str(sold_dollars - bought_dollars),
        "matecoin_account": str(bought_matecoin - sold_matecoin)
    }

    with open("profit.json", "a") as file:
        json.dump(profit, file, indent=2)
