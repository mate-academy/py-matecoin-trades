import json

import decimal


def calculate_profit(trades: str, ):
    with open(trades, "r") as f:
        transactions = json.load(f)
    bought_usd = 0
    sold_usd = 0
    bought_coins = 0
    sold_coins = 0
    for t in transactions:
        if t["bought"]:
            bought_usd += decimal.Decimal(t["bought"]) * \
                decimal.Decimal(t["matecoin_price"])
            bought_coins += decimal.Decimal(t["bought"])
        if t["sold"]:
            sold_usd += decimal.Decimal(t["sold"]) * \
                decimal.Decimal(t["matecoin_price"])
            sold_coins += decimal.Decimal(t["sold"])
    profit = {
        "earned_money": str(sold_usd - bought_usd),
        "matecoin_account": str(bought_coins - sold_coins)
    }
    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
