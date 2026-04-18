from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    money = Decimal("0")
    coins = Decimal("0")
    with open(file_name, "r") as f:
        trades = json.load(f)

    for trade in trades:
        if trade["bought"]:
            money -= (Decimal(trade["bought"])
                      * Decimal(trade["matecoin_price"]))
            coins += Decimal(trade["bought"])

        if trade["sold"]:
            money += (Decimal(trade["sold"])
                      * Decimal(trade["matecoin_price"]))
            coins -= Decimal(trade["sold"])

    result = {
        "earned_money": str(money),
        "matecoin_account": str(coins)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
