from decimal import Decimal
from json import dump, load


def calculate_profit(trade_history):
    sum_profit = 0
    for trade in trade_history:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            sum_profit += Decimal(trade["bought"]) * price
        if trade["sold"]:
            sum_profit -= Decimal(trade["sold"]) * price
    return sum_profit


def calculate_balance_account(trade_history):
    matecoin_account = 0
    for item in trade_history:
        if item["bought"]:
            matecoin_account += Decimal(item["bought"])
        if item["sold"]:
            matecoin_account -= Decimal(item["sold"])
    return matecoin_account


if __name__ == "__main__":
    with open("trades.json", "r") as trade_file:
        trade_history = load(trade_file)

    result = {
        "earned_money": str(calculate_profit(trade_history)),
        "matecoin_account": str(calculate_balance_account(trade_history))
    }

    with open("profit.json", "w") as js_file:
        dump(result, js_file)
