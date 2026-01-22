import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        transactions = json.load(file)

    matecoin_account = Decimal("0.0")
    total_buy_amount = Decimal("0.0")
    total_sell_amount = Decimal("0.0")
    total_buy_value = Decimal("0.0")
    total_sell_value = Decimal("0.0")

    for operation in transactions:
        if operation["bought"] is not None:
            bought_amount = Decimal(operation["bought"])
            price = Decimal(operation["matecoin_price"])
            matecoin_account += bought_amount
            total_buy_amount += bought_amount
            total_buy_value += bought_amount * price

        if operation["sold"] is not None:
            sold_amount = Decimal(operation["sold"])
            price = Decimal(operation["matecoin_price"])
            matecoin_account -= sold_amount
            total_sell_amount += sold_amount
            total_sell_value += sold_amount * price

    total_revenue = total_sell_value - total_buy_value

    with open("profit.json", "w") as file:
        json.dump(
            {
                "earned_money": str(total_revenue),
                "matecoin_account": str(matecoin_account)
            },
            file,
            indent=2
        )


if __name__ == "__main__":
    calculate_profit("trades.json")
