import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        trades = json.load(file)

    earned_money = Decimal()
    matecoin_account = Decimal()

    for trade in trades:
        if trade["bought"] is None:
            sold, matecoin_price = (
                Decimal(trade["sold"]),
                Decimal(trade["matecoin_price"]))

            matecoin_account -= sold
            earned_money += matecoin_price * sold

        elif trade["sold"] is None:
            bought, matecoin_price = (
                Decimal(trade["bought"]),
                Decimal(trade["matecoin_price"]))

            matecoin_account += bought
            earned_money -= matecoin_price * bought

        else:
            bought, sold, matecoin_price = (
                Decimal(trade["bought"]),
                Decimal(trade["sold"]),
                Decimal(trade["matecoin_price"])
            )

            matecoin_account -= sold - bought
            earned_money -= (matecoin_price * bought) - (matecoin_price * sold)

    profit_of_trades = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_of_trades, file, indent=2)
