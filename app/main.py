# write your code here
import json

from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    matecoin_account = Decimal("0")
    earned_money = Decimal("0")
    with open(file_name, "r") as file:
        trades = json.load(file)
    for chaque in trades:
        if chaque["bought"] is not None:
            matecoin_account += Decimal(chaque["bought"])
            earned_money -= (Decimal(chaque["bought"])
                             * Decimal(chaque["matecoin_price"]))
        if chaque["sold"] is not None:
            matecoin_account -= Decimal(chaque["sold"])
            earned_money += (Decimal(chaque["sold"])
                             * Decimal(chaque["matecoin_price"]))

    profit_dict = {"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as file:
        json.dump(profit_dict, file, indent=2)
