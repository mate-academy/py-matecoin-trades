from decimal import Decimal
import json
import os


def calculate_profit(profit_file: None = None) -> None:
    trades_file = "trades.json"
    if not os.path.exists(trades_file):
        print(f"Error: {trades_file} file not found.")
        return None

    with open(trades_file, "r") as f:
        trades = json.load(f)

    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:
        amount = Decimal(trade["amount"])
        price = Decimal(trade["price"])
        fee = Decimal(trade["fee"])

        if trade["type"] == "buy":
            cost = amount * price + fee
            matecoin_account += amount
            earned_money -= cost
        else:
            revenue = amount * price - fee
            matecoin_account -= amount
            earned_money += revenue

    if profit_file is not None:
        with open(profit_file, "w") as f:
            json.dump({
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            }, f)
        return {"earned_money": earned_money,
                "matecoin_account": matecoin_account}
    else:
        return {"earned_money": earned_money,
                "matecoin_account": matecoin_account}


if __name__ == "__main__":
    calculate_profit(profit_file="profit.json")
