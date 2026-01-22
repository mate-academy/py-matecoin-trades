from decimal import Decimal
from json import dump, load


def calculate_profit(file):
    with open(file, "r") as trade_file:
        trade_history = load(trade_file)

    sum_profit = 0
    matecoin_account = 0

    for trade in trade_history:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            sum_profit += Decimal(trade["bought"]) * price
            matecoin_account += Decimal(trade["bought"])
        if trade["sold"]:
            sum_profit -= Decimal(trade["sold"]) * price
            matecoin_account -= Decimal(trade["sold"])

    result = {
        "earned_money": str(sum_profit),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as js_file:
        dump(result, js_file)
