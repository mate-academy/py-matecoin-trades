import json
import decimal
import os


def calculate_profit(filename: str) -> None:
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, "r") as file:
        trades = json.load(file)

    sum_bought = decimal.Decimal("0")
    sum_sold = decimal.Decimal("0")
    account_bought = decimal.Decimal("0")
    account_sold = decimal.Decimal("0")

    for trade in trades:
        if trade["bought"]:
            bought = decimal.Decimal(trade["bought"])
            price = decimal.Decimal(trade["matecoin_price"])
            sum_bought += bought * price
            account_bought += bought
        if trade["sold"]:
            sold = decimal.Decimal(trade["sold"])
            price = decimal.Decimal(trade["matecoin_price"])
            sum_sold += sold * price
            account_sold += sold

    result = {
        "earned_money": str(sum_sold - sum_bought),
        "matecoin_account": str(account_bought - account_sold)
    }

    with open("profit.json", "w") as output_file:
        json.dump(result, output_file, indent=2)


calculate_profit("trades.json")
