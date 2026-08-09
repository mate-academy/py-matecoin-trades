from decimal import Decimal
import json


def calculate_profit(input_json_file: str = "trades.json") -> None:
    with open(input_json_file, "r") as input_info:
        trades_list = json.load(input_info)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    for trade in trades_list:
        if trade.get("bought"):
            earned_money -= (
                Decimal(trade.get("bought"))
                * Decimal(trade.get("matecoin_price"))
            )
            matecoin_account += Decimal(trade.get("bought"))
        if trade.get("sold"):
            earned_money += (
                Decimal(trade.get("sold"))
                * Decimal(trade.get("matecoin_price"))
            )
            matecoin_account -= Decimal(trade.get("sold"))

    final_obj = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as output_info:
        json.dump(final_obj, output_info, indent=2)
