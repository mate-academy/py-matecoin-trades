from decimal import Decimal
import os
import json


file_name = "app/trades.json"


def calculate_profit(file_name: json) -> None:
    data_dict = {}
    bought_price = Decimal(0)
    sell_price = Decimal(0)
    coins_left = 0
    with open(os.path.join(file_name), "r") as file:
        data = json.load(file)
        for coin in data:
            coin_price = Decimal(coin.get("matecoin_price") or 0)
            bought_quantity = Decimal(coin.get("bought") or 0)
            sell_quantity = Decimal(coin.get("sold") or 0)

            bought_price += coin_price * bought_quantity
            sell_price += sell_quantity * coin_price

            coins_left += Decimal(bought_quantity) - Decimal(sell_quantity)

        earned_money = Decimal(sell_price) - Decimal(bought_price)

    with open(os.path.join("profit.json"), "w") as file:
        data_dict["earned_money"] = str(earned_money)
        data_dict["matecoin_account"] = str(coins_left)

        json.dump(data_dict, file, indent=2)


calculate_profit(file_name)
