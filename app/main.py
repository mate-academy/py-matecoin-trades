import json
from decimal import Decimal
import os


def calculate_profit(trades_file: str = "trades.json") -> None:
    if not os.path.exists(trades_file):
        print(f"The file '{trades_file}' does not exist.")
        return

    with open(trades_file, "r") as r:
        trades_data = json.load(r)

    e_mon = Decimal("0")
    mate_c = Decimal("0")

    for trade in trades_data:
        bought = Decimal(trade.get("bought", "0") or "0")
        sold = Decimal(trade.get("sold", "0") or "0")
        mate_price = Decimal(trade["matecoin_price"])

        mate_c += bought
        mate_c -= sold
        e_mon += (sold * mate_price - bought * mate_price)

    result_dict = {
        "earned_money": str(e_mon),
        "matecoin_account": str(mate_c)
    }

    with open("profit.json", "w") as w:
        json.dump(result_dict, w, indent=2)
