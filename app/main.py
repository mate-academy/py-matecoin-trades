import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    with open(trades_file, "r") as source_file:
        trades = json.load(source_file)
    print(trades)
    income = Decimal("0")
    costs = Decimal("0")
    bought_sum = Decimal("0")
    sold_sum = Decimal("0")
    for trade in trades:
        if trade["bought"] is None:
            trade["bought"] = "0"
        if trade["sold"] is None:
            trade["sold"] = "0"
        income += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])
        costs += Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
        bought_sum += Decimal(trade["bought"])
        sold_sum += Decimal(trade["sold"])
    earned_money = income - costs
    matecoin_account = bought_sum - sold_sum
    profit_dict = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}
    print(profit_dict)
    with open("profit.json", "w") as result_file:
        json.dump(profit_dict, result_file, indent=2)
