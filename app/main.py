import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    #  open file
    with open(file_name, "r") as file:
        trades = json.load(file)

    # calculate data
    for trade in trades:
        if trade["bought"] is not None:
            matecoin_account += Decimal(trade["bought"])
            earned_money -= (Decimal(trade["bought"])
                             * Decimal(trade["matecoin_price"]))
        if trade["sold"] is not None:
            matecoin_account -= Decimal(trade["sold"])
            earned_money += (Decimal(trade["sold"])
                             * Decimal(trade["matecoin_price"]))

    #  save file
    string_to_save = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)}
    with open("profit.json", "w") as file:
        json.dump(string_to_save, file, indent=2)
