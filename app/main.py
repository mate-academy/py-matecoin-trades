import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    earned_money = Decimal("0")
    matecoin_account = Decimal("0")
    with open(filename, "r") as file_in, open("profit.json", "w") as file_out:
        trade_info = json.load(file_in)
        for trade in trade_info:
            if trade["bought"]:
                earned_money -= change_coin(
                    trade["bought"],
                    trade["matecoin_price"]
                )
                matecoin_account += Decimal(str(trade["bought"]))
            if trade["sold"]:
                earned_money += change_coin(
                    trade["sold"],
                    trade["matecoin_price"]
                )
                matecoin_account -= Decimal(str(trade["sold"]))
        profit_dict = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        json.dump(profit_dict, file_out, indent=2)


def change_coin(coin: Decimal, currency: Decimal) -> Decimal:
    return Decimal(str(coin)) * Decimal(str(currency))
