import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:

    with open(file_name, "r") as history:
        trades_history = json.load(history)

    total_spent = Decimal(0)
    matecoin_account = Decimal(0)
    for trade in trades_history:
        if trade["bought"]:
            matecoin_volume = Decimal(trade["bought"])
            matecoin_price = Decimal(trade["matecoin_price"])
            total_spent += matecoin_volume * matecoin_price
            matecoin_account += matecoin_volume

        if trade["sold"]:
            matecoin_volume = Decimal(trade["sold"])
            matecoin_price = Decimal(trade["matecoin_price"])
            total_spent -= matecoin_volume * matecoin_price
            matecoin_account -= matecoin_volume

    earned_money = str(0 - total_spent)
    matecoin_account = str(matecoin_account)

    with open("profit.json", "w") as earned:
        json.dump({"earned_money": earned_money,
                   "matecoin_account": matecoin_account}, earned, indent=2)
