import json
from decimal import Decimal


def calculate_profit(reading_file_path: str) -> None:
    spend = 0
    earned = 0
    bought_amount = 0
    sold_amount = 0
    with open(reading_file_path, "r") as f:
        coins_data = json.load(f)
    for trade in coins_data:
        if trade["bought"]:
            bought_amount += Decimal(trade["bought"])
            spend = spend + spendings_calculation(trade["bought"],
                                                  trade["matecoin_price"])
        if trade["sold"]:
            sold_amount += Decimal(trade["sold"])
            earned = earned + earnings_calculation(trade["sold"],
                                                   trade["matecoin_price"])
    json_profit = {
        "earned_money": str(earned - spend),
        "matecoin_account": str(bought_amount - sold_amount)
    }
    with open("profit.json", "w") as f:
        json.dump(json_profit, f, indent=2)


def spendings_calculation(value_bought: str,
                          value_coins: str) -> Decimal:
    return Decimal(value_bought) * Decimal(value_coins)


def earnings_calculation(value_bought: str,
                         value_coins: str) -> Decimal:
    return Decimal(value_bought) * Decimal(value_coins)
