import json
from decimal import Decimal


def calculate_profit(file_name):
    with open(file_name) as trades_file:
        trade_list = json.load(trades_file)

    matecoin_account = 0
    earned_money = 0

    for trade in trade_list:
        price = Decimal(trade["matecoin_price"])
        if trade["bought"]:
            bought = Decimal(trade["bought"])
            matecoin_account += bought
            earned_money -= bought * price
        if trade["sold"]:
            sold = Decimal(trade["sold"])
            matecoin_account -= sold
            earned_money += sold * price

    trading_result = {"earned_money": str(earned_money),
                      "matecoin_account": str(matecoin_account)}

    with open("profit.json", "w") as profit_file:
        json.dump(trading_result, profit_file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
