import json
from _decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        trades = json.load(json_file)

    current_account = 0
    earned_money = 0

    for trade in trades:
        if trade["bought"] is not None and trade["sold"] is None:
            money_for_trade = (Decimal(trade["bought"])
                               * Decimal(trade["matecoin_price"]))
            earned_money -= money_for_trade
            current_account += Decimal(trade["bought"])
        elif trade["sold"] is not None and trade["bought"] is None:
            money_for_trade = (Decimal(trade["sold"])
                               * Decimal(trade["matecoin_price"]))
            earned_money += money_for_trade
            current_account -= Decimal(trade["sold"])
        else:
            money_for_trade = (Decimal(trade["sold"])
                               * Decimal(trade["matecoin_price"])
                               - Decimal(trade["bought"])
                               * Decimal(trade["matecoin_price"]))
            earned_money += money_for_trade
            current_account += (Decimal(trade["bought"])
                                - Decimal(trade["sold"]))

    earned_money = str(Decimal(earned_money))
    matecoin_account = str(Decimal(current_account))

    profit_dict = {
        "earned_money": earned_money,
        "matecoin_account": matecoin_account
    }

    with open("profit.json", "w") as profit_json:
        json.dump(profit_dict, profit_json, indent=2)
