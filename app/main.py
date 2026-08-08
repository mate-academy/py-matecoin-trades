import decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        trades = json.load(file)
    profit = decimal.Decimal(0)
    matecoin_amount = decimal.Decimal(0)
    for trade in trades:
        if trade["bought"]:
            profit -= decimal.Decimal(trade["bought"]) * decimal.Decimal(trade["matecoin_price"])
            matecoin_amount += decimal.Decimal(trade["bought"])
        if trade["sold"]:
            profit += decimal.Decimal(trade["sold"]) * decimal.Decimal(trade["matecoin_price"])
            matecoin_amount -= decimal.Decimal(trade["sold"])
    profit_dict = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_amount)
    }
    with open("profit.json", "w") as file:
        json.dump(profit_dict, file)
