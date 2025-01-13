import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        daily_trades = json.load(file)
    daily_profit = []
    daily_account = []
    for trade in daily_trades:
        if trade["sold"] and trade["bought"]:
            profit = (
                (Decimal(trade["sold"]) - Decimal(trade["bought"]))
                * Decimal(trade["matecoin_price"])
            )
        elif trade["sold"]:
            profit = (
                Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
            )
        elif trade["bought"]:
            profit = (
                - Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
            )
        daily_profit.append(profit)
        if trade["bought"] and trade["sold"]:
            account = Decimal(trade["bought"]) - Decimal(trade["sold"])
        elif trade["bought"]:
            account = Decimal(trade["bought"])
        elif trade["sold"]:
            account = - Decimal(trade["sold"])
        daily_account.append(account)
    total_profit = sum(daily_profit)
    matecoin_account = sum(daily_account)
    profit_dict = {
        "earned_money": str(total_profit),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        profit = json.dump(profit_dict, file, indent=2)
