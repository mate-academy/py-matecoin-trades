import json
from _decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename) as f:
        trades = json.load(f)
        arr_dict = {}
        earned_money = Decimal(0)
        matecoin_account = Decimal(0)

        for trade in trades:
            if trade["bought"]:
                earned_money -= (Decimal(trade["bought"])
                                 * Decimal(trade["matecoin_price"]))
                matecoin_account += Decimal(trade["bought"])
            if trade["sold"]:
                earned_money += (Decimal(trade["sold"])
                                 * Decimal(trade["matecoin_price"]))
                matecoin_account -= Decimal(trade["sold"])

        arr_dict["earned_money"] = str(earned_money)
        arr_dict["matecoin_account"] = str(matecoin_account)
        with open("profit.json", "w") as wr:
            json.dump(arr_dict, wr, indent=2)
