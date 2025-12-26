import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades_info = json.load(file)

    balance_matecoin = 0
    balance_usdt = 0

    for trade_info in trades_info:
        price = Decimal(trade_info["matecoin_price"])

        if trade_info["bought"]:
            bought = Decimal(trade_info["bought"])
            balance_matecoin += bought
            balance_usdt -= price * bought
        if trade_info["sold"]:
            sold = Decimal(trade_info["sold"])
            balance_matecoin -= sold
            balance_usdt += price * sold

    result = {
        "earned_money": str(balance_usdt),
        "matecoin_account": str(balance_matecoin)
    }

    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
