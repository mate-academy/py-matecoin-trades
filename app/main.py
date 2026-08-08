from decimal import Decimal
import json


def calculate_profit(trade_data: str) -> None:
    with open(trade_data) as file:
        trade_dict = json.load(file)

    profit = 0
    matecoin_account = 0

    for trade in trade_dict:
        matecoin_price = Decimal(trade["matecoin_price"])

        if trade.get("bought"):
            matecoin_account += Decimal(trade["bought"])
            profit -= Decimal(trade["bought"]) * matecoin_price
        if trade.get("sold"):
            matecoin_account -= Decimal(trade["sold"])
            profit += Decimal(trade["sold"]) * matecoin_price

    profit_data = {
        "earned_money": str(profit),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(profit_data, file, indent=2)
