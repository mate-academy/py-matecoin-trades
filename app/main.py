import json
from decimal import Decimal


def calculate_profit(trades_file: str = "trades.json",
                     output_file: str = "profit.json") -> None:
    with open(trades_file) as file:
        trades = json.load(file)

    total_money = Decimal("0")
    matecoin_balance = Decimal("0")

    for trade in trades:
        bought_volume = Decimal(trade["bought"]) if trade["bought"] \
            else Decimal("0")
        sold_volume = Decimal(trade["sold"]) if trade["sold"] else Decimal("0")
        matecoin_price = Decimal(trade["matecoin_price"])
        if bought_volume:
            total_money -= bought_volume * matecoin_price
            matecoin_balance += bought_volume
        if sold_volume:
            total_money += sold_volume * matecoin_price
            matecoin_balance -= sold_volume

    result = {
        "earned_money": str(total_money),
        "matecoin_account": str(matecoin_balance)
    }
    with open(output_file, "w") as result_file:
        json.dump(result, result_file, indent=2)
