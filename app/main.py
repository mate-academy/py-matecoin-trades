import decimal
import json


def calculate_profit(name):
    coins = 0
    lose_money = 0
    earn_money = 0
    with open(name, "r") as f:
        trades = json.load(f)
    for trade in trades:
        price = decimal.Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            bought_coins = decimal.Decimal(trade["bought"])
            lose_money += bought_coins * price
            coins += bought_coins
        if trade["sold"] is not None:
            sold_coins = decimal.Decimal(trade["sold"])
            earn_money += sold_coins * price
            coins -= sold_coins

    with open("profit.json", "w") as f:
        json.dump({"earned_money": str(earn_money - lose_money),
                   "matecoin_account": str(coins)}, f, indent=2)
