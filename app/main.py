import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        file_information = json.load(file)
    coins = 0
    purchased_money = 0
    for info_file in file_information:
        if info_file["bought"] is not None:
            purchased_money -= (Decimal(info_file["bought"])
                                * Decimal(info_file["matecoin_price"]))
            coins += Decimal(info_file["bought"])
        if info_file["sold"] is not None:
            purchased_money += (Decimal(info_file["sold"])
                                * Decimal(info_file["matecoin_price"]))
            coins -= Decimal(info_file["sold"])
    income = {
        "earned_money": str(purchased_money),
        "matecoin_account": str(coins)
    }
    with open("profit.json", "w") as file:
        json.dump(income, file, indent=2)
