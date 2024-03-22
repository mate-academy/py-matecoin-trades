from decimal import Decimal
import json


def calculate_profit(trade_data: str) -> None:
    with open(trade_data, "r") as file:
        trades = json.load(file)

    money = Decimal(0)
    matecoin_account = Decimal(0)

    for trade in trades:
        if trade.get("bought"):
            bought = Decimal(trade["bought"])
            matecoin_prise = Decimal(trade["matecoin_price"])
            money -= bought * matecoin_prise
            matecoin_account += bought

        if trade.get("sold"):
            sold = Decimal(trade["sold"])
            matecoin_prise = Decimal(trade["matecoin_price"])
            money += sold * matecoin_prise
            matecoin_account -= sold
    result = {
        "earned_money": str(money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
