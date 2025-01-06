import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        trades = json.load(f)
        coins = 0
        profit = 0
        for trade in trades:
            if trade["bought"]:
                coins += decimal.Decimal(trade["bought"])
                profit -= (decimal.Decimal(trade["bought"])
                           * decimal.Decimal(trade["matecoin_price"]))
            if trade["sold"]:
                coins -= decimal.Decimal(trade["sold"])
                profit += (decimal.Decimal(trade["sold"])
                           * decimal.Decimal(trade["matecoin_price"]))
        profit_dict = {
            "earned_money": str(profit),
            "matecoin_account": str(coins)
        }
        with open("profit.json", "w") as file:
            json.dump(profit_dict, file, indent=2)
