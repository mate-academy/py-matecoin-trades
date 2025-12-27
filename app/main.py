from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    with open(filename) as f:
        trades_data = json.load(f)
    result_dict = {}
    coins = 0
    money = 0
    for days in trades_data:
        if days["bought"]:
            coins += Decimal(days["bought"])
            money -= Decimal(days["bought"]) * Decimal(days["matecoin_price"])
        if days["sold"]:
            coins -= Decimal(days["sold"])
            money += Decimal(days["sold"]) * Decimal(days["matecoin_price"])
    result_dict["earned_money"] = str(money)
    result_dict["matecoin_account"] = str(coins)
    with open("profit.json", "w") as f:
        json.dump(result_dict, f, indent=2)
