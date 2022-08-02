import json
import decimal


def calculate_profit(file_name: str):
    with open(file_name, "r") as f:
        trades_data = json.load(f)

    bought_usd = 0
    sold_usd = 0
    bought_coins = 0
    sold_coins = 0

    for trade in trades_data:
        if trade["bought"]:
            bought_usd += decimal.Decimal(trade["bought"])\
                * decimal.Decimal(trade["matecoin_price"])
            bought_coins += decimal.Decimal(trade["bought"])
        if trade["sold"]:
            sold_usd += decimal.Decimal(trade["sold"])\
                * decimal.Decimal(trade["matecoin_price"])
            sold_coins += decimal.Decimal(trade["sold"])

    profit = {
        "earned_money": str(sold_usd - bought_usd),
        "matecoin_account": str(bought_coins - sold_coins)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
