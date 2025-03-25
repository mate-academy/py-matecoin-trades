import json
from decimal import Decimal


def calculate_profit(name: str) -> None:
    with open(name, "r") as file:
        dictin = json.load(file)
    minus = 0
    plus = 0
    coin_acc = 0
    for dic in dictin:
        if dic["bought"] is not None:
            defit = Decimal(dic["bought"]) * Decimal(dic["matecoin_price"])
            minus += defit
            coin_acc += Decimal(dic["bought"])
        if dic["sold"] is not None:
            profit = Decimal(dic["sold"]) * Decimal(dic["matecoin_price"])
            plus += profit
            coin_acc -= Decimal(dic["sold"])
    new_d = {"earned_money" : str(plus - minus),
             "matecoin_account": str(coin_acc)}
    with open("profit.json", "w") as f:
        json.dump(new_d, f, indent=2)
