import json
import decimal


def calculate_profit(trades_file_path: str) -> None:
    with open(trades_file_path, "r") as trades_file:
        trades = json.load(trades_file)

    total_spent = decimal.Decimal(0.0)
    total_received = decimal.Decimal(0.0)
    matecoin_balance = decimal.Decimal(0.0)

    for trade in trades:
        if trade["bought"] is not None:
            bought = decimal.Decimal(trade["bought"])
            price = decimal.Decimal(trade["matecoin_price"])
            total_spent += bought * price
            matecoin_balance += bought
        if trade["sold"] is not None:
            sold = decimal.Decimal(trade["sold"])
            price = decimal.Decimal(trade["matecoin_price"])
            total_received += sold * price
            matecoin_balance -= sold

    money = total_received - total_spent
    result = {
        "earned_money": str(money),
        "matecoin_account": str(matecoin_balance),
    }

    with open("profit.json", "w") as profit_file:
        json.dump(result, profit_file, indent=2)