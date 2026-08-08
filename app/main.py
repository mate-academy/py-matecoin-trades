import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    coin_amount = 0
    money_waste = 0

    for transaction in trades:
        if transaction["bought"]:
            money_waste -= Decimal(transaction["bought"]) * Decimal(
                transaction["matecoin_price"]
            )
            coin_amount += Decimal(transaction["bought"])
        if transaction["sold"]:
            money_waste += Decimal(transaction["sold"]) * Decimal(
                transaction["matecoin_price"]
            )
            coin_amount -= Decimal(transaction["sold"])

    result = {
        "earned_money": str(money_waste),
        "matecoin_account": str(coin_amount)
    }

    with open("profit.json", "w") as profit:
        json.dump(result, profit, indent=2)


if __name__ == "__main__":
    print(
        calculate_profit(
            "/home/acidcor/PycharmProjects/py-matecoin-trades/app/trades.json"
        )
    )
