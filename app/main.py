import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    with open(name) as f:
        data = json.load(f)

    money = 0
    coins = 0

    for trade in data:
        if "bought" in trade and trade["bought"] is not None:
            bought_coin = Decimal(trade["bought"])
            price = Decimal(trade["matecoin_price"])
            profit_by_day = bought_coin * price
            money -= profit_by_day
            coins += bought_coin
        if "sold" in trade and trade["sold"] is not None:
            sold_coin = Decimal(trade["sold"])
            profit_by_day = sold_coin * Decimal(trade["matecoin_price"])
            money += profit_by_day
            coins -= sold_coin

    result_string = {
        "earned_money": str(money),
        "matecoin_account": str(coins)}
    with open("profit.json", "w") as file:
        json.dump(result_string, file, indent=2)


if __name__ == "__main__":
    result = calculate_profit()
    print(result)
