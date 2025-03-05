import json
import decimal


def calculate_profit(path: str) -> None:
    profit = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    with open(path, "r") as file:
        trades_list = json.load(file)

        for trade in trades_list:
            matecoin_price = decimal.Decimal(trade["matecoin_price"])
            if trade.get("bought"):

                amount = decimal.Decimal(trade["bought"])
                spent_money = matecoin_price * amount

                profit["matecoin_account"] += amount
                profit["earned_money"] -= spent_money

            if trade.get("sold"):

                amount = decimal.Decimal(trade["sold"])
                earned_money = matecoin_price * amount

                profit["matecoin_account"] -= amount
                profit["earned_money"] += earned_money

    profit_serializable = {
        "earned_money": str(profit["earned_money"]),
        "matecoin_account": str(profit["matecoin_account"])
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit_serializable, profit_file, indent=2)
