from decimal import Decimal
import json
import os


def calculate_profit(trades: str) -> None:

    with open(trades, "r") as file:
        new_trades = json.load(file)

        earned_money = Decimal(0)
        matecoin_account = Decimal(0)

        for trade in new_trades:
            decimal_trade = Decimal(trade["matecoin_price"])
            if trade["bought"] is not None:
                decimal_bought = Decimal(trade["bought"])
                matecoin_account += decimal_bought
                earned_money -= decimal_bought * decimal_trade
            if trade["sold"] is not None:
                decimal_sold = Decimal(trade["sold"])
                matecoin_account -= decimal_sold
                earned_money += decimal_sold * decimal_trade

    profit_os_path = os.path.join(os.path.dirname(__file__), "PROFIT.json")

    with open(profit_os_path, "w", encoding="utf-8") as file_2:
        json.dump({"earned_money": str(earned_money),
                   "matecoin_account": str(matecoin_account)},
                  file_2, indent=4)
