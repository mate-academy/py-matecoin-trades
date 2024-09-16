import json
from decimal import Decimal


def calculate_profit(name_of_file: str) -> None:
    with open(name_of_file) as file_in:
        trades_description = json.load(file_in)

    matecoin_account = 0
    earned_money = 0
    for trade in trades_description:
        if trade["bought"] is None:
            trade["bought"] = Decimal("0")
        elif trade["sold"] is None:
            trade["sold"] = Decimal("0")
        matecoin_account_for_trade = \
            Decimal(trade["bought"]) - Decimal(trade["sold"])
        matecoin_account += matecoin_account_for_trade
        earned_money_for_trade = \
            Decimal(trade["sold"]) * Decimal(trade["matecoin_price"]) - \
            Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
        earned_money += earned_money_for_trade

    profit_str = {"earned_money": str(earned_money),
                  "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as file_out:
        json.dump(profit_str, file_out, indent=2)
