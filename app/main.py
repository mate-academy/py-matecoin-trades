import json
from decimal import Decimal


def calculate_profit(file_path: str) -> None:
    with open(file_path, "r") as file:
        matecoin_trades = json.load(file)

    bought_usdt = []
    sold_usdt = []
    bought_matecoin = []
    sold_matecoin = []
    for trade in matecoin_trades:
        if trade["bought"]:
            bought_usdt.append(
                Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )
            bought_matecoin.append(Decimal(trade["bought"]))

        if trade["sold"]:
            sold_usdt.append(
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )
            sold_matecoin.append(Decimal(trade["sold"]))

    total_profit = str(
        sum(sold_usdt, Decimal("0")) - sum(bought_usdt, Decimal("0"))
    )
    total_crypto = str(
        sum(bought_matecoin, Decimal("0")) - sum(sold_matecoin, Decimal("0"))
    )
    result = {"earned_money": total_profit, "matecoin_account": total_crypto}

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
