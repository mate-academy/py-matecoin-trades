import json
from decimal import Decimal


def calculate_profit(trades: str) -> None:
    buying = 0
    selling = 0
    account = 0
    with open(trades, "r") as trades:
        trades_info = json.load(trades)
        for trade in trades_info:
            price = Decimal(trade["matecoin_price"])
            if trade["bought"]:
                buying += Decimal(trade["bought"]) * price
                account += Decimal(trade["bought"])
            if trade["sold"]:
                selling += Decimal(trade["sold"]) * price
                account -= Decimal(trade["sold"])
    profit_dict = {
        "earned_money": str(selling - buying),
        "matecoin_account": str(account)
    }
    with open("profit.json", "w") as profit:
        json.dump(profit_dict, profit, indent=2)
