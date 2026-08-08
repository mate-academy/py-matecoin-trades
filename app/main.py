import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    result = {"earned_money": "", "matecoin_account": ""}
    bought = 0
    sold = 0
    earn_money = 0
    with open(file_name, "r") as file:
        coin_information = json.load(file)
        for item in coin_information:
            bought_value = item.get("bought") or "0"
            bought += Decimal(bought_value)
            sold_value = item.get("sold") or "0"
            sold += Decimal(sold_value)
            mate_coin = item["matecoin_price"]
            earn_money += (
                Decimal(mate_coin) * Decimal(sold_value)
                - Decimal(mate_coin) * Decimal(bought_value)
            )
    result["earned_money"] = str(earn_money)
    result["matecoin_account"] = str(bought - sold)
    with open("profit.json", "w") as writing_file:
        json.dump(result, writing_file, indent=2)
