import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    total_profit = Decimal("0.0")
    matecoin_balance = Decimal("0.0")

    for trade in trades:
        bought = trade.get("bought")
        sold = trade.get("sold")
        matecoin_price = Decimal(trade["matecoin_price"])

        if bought:
            matecoin_balance += Decimal(bought)
            total_profit -= Decimal(bought) * matecoin_price
        if sold:
            total_profit += Decimal(sold) * matecoin_price
            matecoin_balance -= Decimal(sold)

    result = {
        "earned_money": str(total_profit),
        "matecoin_account": str(matecoin_balance)
    }

    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
