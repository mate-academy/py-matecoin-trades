import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    with open(file_path, "r", encoding="utf-8") as f:
        trades = json.load(f)

    total_money = Decimal("0")
    total_coins = Decimal("0")

    for trade in trades:
        price = Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = Decimal(trade["bought"])
            total_coins += bought
            total_money -= bought * price

        if trade["sold"] is not None:
            sold = Decimal(trade["sold"])
            total_coins -= sold
            total_money += sold * price

    result = {
        "earned_money": str(total_money),
        "matecoin_account": str(total_coins),
    }

    # input in terminal
    print(json.dumps(result, indent=2))

    # save in file
    with open("profit.json", "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)


calculate_profit("app/trades.json")
