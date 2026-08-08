import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as f:
        trades_data = json.load(f)

    money = Decimal("0")
    coin = Decimal("0")
    for trade in trades_data:
        if trade["bought"]:
            coin += Decimal(trade["bought"])
            money -= (Decimal(trade["bought"])
                      * Decimal(trade["matecoin_price"]))
        if trade["sold"]:
            coin -= Decimal(trade["sold"])
            money += (Decimal(trade["sold"])
                      * Decimal(trade["matecoin_price"]))

    result = {
        "earned_money": str(money),
        "matecoin_account": str(coin)
    }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
