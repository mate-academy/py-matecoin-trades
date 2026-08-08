import json
from decimal import Decimal


def calculate_profit(file_name: str, output_file: str = "profit.json") -> None:
    with open(file_name, "r") as file_in:
        trades_info = json.load(file_in)

    earned = Decimal("0")
    coin_account = Decimal("0")

    for trade in trades_info:
        if "bought" in trade and trade["bought"]:
            earned -= (Decimal(trade["bought"])
                       * Decimal(trade["matecoin_price"]))
            coin_account += Decimal(trade["bought"])
        if "sold" in trade and trade["sold"]:
            earned += (Decimal(trade["sold"])
                       * Decimal(trade["matecoin_price"]))
            coin_account -= Decimal(trade["sold"])

    profit = {
        "earned_money": f"{earned}",
        "matecoin_account": f"{coin_account}"
    }

    with open(output_file, "w") as file_out:
        json.dump(profit, file_out, indent=2)
