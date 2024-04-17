import json
from decimal import Decimal


def calculate_profit(trades_information_file: str) -> None:
    with open(trades_information_file, "r") as file:
        trades = json.load(file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade["bought"]) if (trade.get("bought")
                                              is not None) else Decimal("0")
        sold = Decimal(trade["sold"]) if (trade.get("sold")
                                          is not None) else Decimal("0")
        matecoin_price = Decimal(trade["matecoin_price"])

        earned_money += sold * matecoin_price
        earned_money -= bought * matecoin_price
        matecoin_account += bought
        matecoin_account -= sold

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as outfile:
        json.dump(profit_data, outfile, indent=2)
