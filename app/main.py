import decimal
import json


def calculate_profit(file_name: str) -> None:
    earned_money = 0
    matecoin_account = 0
    with open(file_name, "r") as file:
        metcoin_data = json.load(file)
    for trade in metcoin_data:
        if trade.get("bought"):
            matecoin_account += decimal.Decimal(trade["bought"])
            earned_money -= decimal.Decimal(trade["bought"]) * decimal.Decimal(
                trade["matecoin_price"]
            )
        if trade.get("sold"):
            matecoin_account -= decimal.Decimal(trade["sold"])
            earned_money += decimal.Decimal(trade["sold"]) * decimal.Decimal(
                trade["matecoin_price"]
            )
    profit_info = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }
    metcoin_data.append(profit_info)
    with open("profit.json", "w") as file:
        json.dump(profit_info, file, indent=2)
