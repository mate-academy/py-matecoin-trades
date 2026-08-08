import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    money_result = Decimal("0.0")
    coin_result = Decimal("0.0")

    with open(file_name, "r") as file:
        trade_operations = json.load(file)

        for trade in trade_operations:
            price = Decimal(trade["matecoin_price"])

            if trade["bought"]:
                how_much_bought = Decimal(trade["bought"])

                money_result -= how_much_bought * price

                coin_result += how_much_bought

            if trade["sold"]:
                how_much_sold = Decimal(trade["sold"])

                money_result += how_much_sold * price

                coin_result -= how_much_sold

    result = {"earned_money": str(money_result),
              "matecoin_account": str(coin_result)}

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
