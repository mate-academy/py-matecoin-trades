import json
from decimal import Decimal


def calculate_profit(trade_file_name: str) -> None:
    with open(trade_file_name, "r") as trade_file:
        trade_data = json.load(trade_file)

    profit_coins = Decimal("0")
    profit_dollars = Decimal("0")

    for operation_data in trade_data:
        price = Decimal(operation_data["matecoin_price"])

        if operation_data["bought"] is not None:
            bought = Decimal(operation_data["bought"])
            profit_coins += bought
            profit_dollars -= bought * price

        if operation_data["sold"] is not None:
            sold = Decimal(operation_data["sold"])
            profit_coins -= sold
            profit_dollars += sold * price

    result_dict = {
        "earned_money": str(profit_dollars),
        "matecoin_account": str(profit_coins)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(result_dict, profit_file, indent=2)
