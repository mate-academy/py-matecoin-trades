import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    trades = open(file_name, "r")
    trades_list = json.load(trades)
    earned_money = 0
    matecoin_account = 0
    for trade in trades_list:
        if trade["sold"] is not None:
            matecoin_trade = Decimal(trade["sold"])
            earned_money += matecoin_trade * Decimal(trade["matecoin_price"])
            matecoin_account -= matecoin_trade
        if trade["bought"] is not None:
            matecoin_trade = Decimal(trade["bought"])
            earned_money -= matecoin_trade * Decimal(trade["matecoin_price"])
            matecoin_account += matecoin_trade

    with open("profit.json", "w") as profit_file:
        json.dump({
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }, profit_file, indent=2)
