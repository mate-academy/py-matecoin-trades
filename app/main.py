import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r", newline="", encoding="utf-8") as f:
        dataset = json.load(f)
    total_bought_coins = Decimal(0)
    total_sold_coins = Decimal(0)
    total_spent_dollars = Decimal(0)
    total_earned_dollars = Decimal(0)
    for dict_with_coin in dataset:
        if dict_with_coin["bought"] is not None:
            total_bought_coins += Decimal(dict_with_coin["bought"])
            total_spent_dollars += (
                    Decimal(dict_with_coin["bought"]) *
                    Decimal(dict_with_coin["matecoin_price"]))
        if dict_with_coin["sold"] is not None:
            total_sold_coins += Decimal(dict_with_coin["sold"])
            total_earned_dollars += (
                    Decimal(dict_with_coin["sold"]) *
                    Decimal(dict_with_coin["matecoin_price"]))
    earned_money = total_earned_dollars - total_spent_dollars
    matecoin_account = total_bought_coins - total_sold_coins
    with open("profit.json", "w", newline="", encoding="utf-8") as f:
        json.dump({"earned_money": f"{earned_money}",
                   "matecoin_account": f"{matecoin_account}"}, f, indent=2)
