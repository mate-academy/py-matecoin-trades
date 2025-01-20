import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as file:
        trades = json.load(file)

    money = Decimal("0")
    matecoin = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"] or "0")
        sold = Decimal(trade["sold"] or "0")
        price = Decimal(trade["matecoin_price"])

        money -= bought * price
        money += sold * price
        matecoin += bought
        matecoin -= sold

    result = {
        "earned_money": str(money),
        "matecoin_account": str(matecoin)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)

    print("Файл profit.json успішно стрворений.")


calculate_profit("./app/trades.json")
