import json
from decimal import Decimal, getcontext


def calculate_profit(filename: str) -> None:
    getcontext().prec = 10  # встановлюємо точність обчислень

    with open(filename, "r", encoding="utf-8") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade["bought"]:
            bought_amount = Decimal(trade["bought"])
            matecoin_account += bought_amount
            earned_money -= bought_amount * matecoin_price

        if trade["sold"]:
            sold_amount = Decimal(trade["sold"])
            matecoin_account -= sold_amount
            earned_money += sold_amount * matecoin_price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w", encoding="utf-8") as output_file:
        json.dump(result, output_file, indent=2)

    print(json.dumps(result, indent=2))
