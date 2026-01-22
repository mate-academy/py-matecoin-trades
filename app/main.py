import json
from decimal import Decimal


def none_to_null(number: Decimal | int | float | None) -> Decimal:
    if number is None:
        return Decimal(0)
    return Decimal(number)


def calculate_profit(trades_json: str) -> None:
    with open(trades_json, "r") as file_json:
        trades = json.load(file_json)
    print(trades)
    bought_total = none_to_null(0)
    sold_total = none_to_null(0)
    earned_money = 0
    for trade in trades:
        bought = Decimal(none_to_null(trade["bought"]))
        sold = Decimal(none_to_null(trade["sold"]))
        matecoin_price = Decimal(none_to_null(trade["matecoin_price"]))
        earned_money += (sold - bought) * matecoin_price
        bought_total += bought
        sold_total += sold
    matecoin_account = none_to_null(bought_total - sold_total)
    profit = {"earned_money": str(earned_money),
              "matecoin_account": str(matecoin_account)}
    # profit_json = []
    # profit_json.append(profit)
    # print(profit_json)
    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
