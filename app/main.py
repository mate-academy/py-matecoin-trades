import decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trade_data = json.load(f)
    bought_money, sold_money, bought_coins, sold_coins = 0, 0, 0, 0
    for day in trade_data:
        if day["bought"]:
            bought_money += (decimal.Decimal(day["bought"])
                             * decimal.Decimal(day["matecoin_price"]))
            bought_coins += decimal.Decimal(day["bought"])
        if day["sold"]:
            sold_money += (decimal.Decimal(day["sold"])
                           * decimal.Decimal(day["matecoin_price"]))
            sold_coins += decimal.Decimal(day["sold"])
    profit_data = {
        "earned_money": str(sold_money - bought_money),
        "matecoin_account": str(bought_coins - sold_coins)
    }
    with open("profit.json", "w") as f:
        json.dump(profit_data, f, indent=2)
