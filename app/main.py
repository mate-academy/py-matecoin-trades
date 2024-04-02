import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as trades:
        trade_data = json.load(trades)

    coins_bought = dollars_spent = coins_sold = dollars_earned = Decimal("0")

    for trade in trade_data:
        if trade.get("bought"):
            coins_bought += Decimal(trade["bought"])
            money_spent = (Decimal(trade["bought"])
                           * Decimal(trade["matecoin_price"]))
            dollars_spent += money_spent
        if trade.get("sold"):
            coins_sold += Decimal(trade["sold"])
            money_earned = (Decimal(trade["sold"])
                            * Decimal(trade["matecoin_price"]))
            dollars_earned += money_earned

    earned_money = str(dollars_earned - dollars_spent)
    matecoin_account = str(coins_bought - coins_sold)
    profit = {
        "earned_money": earned_money,
        "matecoin_account": matecoin_account
    }

    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
