import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename) as input_file:
        trades = json.load(input_file)

    dollar_account = Decimal()
    matecoin_account = Decimal()
    for trade in trades:
        if trade["bought"]:
            matecoin_value = Decimal(trade["bought"])
            matecoin_account += matecoin_value
            dollar_account -= matecoin_value * Decimal(trade["matecoin_price"])
        if trade["sold"]:
            matecoin_value = Decimal(trade["sold"])
            matecoin_account -= matecoin_value
            dollar_account += matecoin_value * Decimal(trade["matecoin_price"])

    with open("profit.json", "w") as profit_file:
        json.dump({
            "earned_money": format(dollar_account, "f"),
            "matecoin_account": format(matecoin_account, "f"),
        }, profit_file, indent=2)
