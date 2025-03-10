import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    bought_info = 0
    sold_info = 0
    bought_coins = 0
    sold_coins = 0

    with open(trades_file, "r") as f:
        trade_data = json.load(f)
        print(trade_data)

    for trade_info in trade_data:
        if trade_info["bought"] is not None:
            bought_coins += Decimal(trade_info["bought"])
            bought_info += (Decimal(trade_info["bought"])
                            * Decimal(trade_info["matecoin_price"]))
        if trade_info["sold"] is not None:
            sold_coins += Decimal(trade_info["sold"])
            sold_info += (Decimal(trade_info["sold"])
                          * Decimal(trade_info["matecoin_price"]))

    income = str(sold_info - bought_info)
    total_coins = str(bought_coins - sold_coins)

    profit_data = {"earned_money": income, "matecoin_account": total_coins}

    with open("profit.json", "a") as f:
        json.dump(profit_data, f, indent=2)
