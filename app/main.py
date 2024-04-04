import json
from decimal import Decimal


def calculate_profit(trades_file_name: str = "trades.json") -> None:
    with open(trades_file_name, "r") as file:
        trades = json.load(file)

    total_profit_dollars = Decimal("0.0")
    current_coin_balance = Decimal("0.0")

    for transaction in trades:
        bought = transaction["bought"]
        sold = transaction["sold"]
        matecoin_price = Decimal(transaction["matecoin_price"])

        if bought is not None:
            bought_amount = Decimal(bought)
            current_coin_balance += bought_amount
            total_profit_dollars -= bought_amount * matecoin_price

        if sold is not None:
            sold_amount = Decimal(sold)
            current_coin_balance -= sold_amount
            total_profit_dollars += sold_amount * matecoin_price

    profit_data = {
        "earned_money": str(total_profit_dollars.normalize()),
        "matecoin_account": str(current_coin_balance.normalize())
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file, ensure_ascii=False, indent=2)
