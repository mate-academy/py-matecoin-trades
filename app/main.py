import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

    total_invested = Decimal(0)
    total_received = Decimal(0)
    total_bought = Decimal(0)
    total_sold = Decimal(0)

    for trade in trades:

        trade_coin = Decimal(trade["matecoin_price"])

        if trade["sold"] is None:
            trade_bought = Decimal(trade["bought"])
            total_invested += trade_bought * trade_coin
            total_bought += trade_bought

        if trade["bought"] is None:
            trade_sold = Decimal(trade["sold"])
            total_received += trade_sold * trade_coin
            total_sold += trade_sold

        if trade["bought"] and trade["sold"]:
            trade_bought = Decimal(trade["bought"])
            trade_sold = Decimal(trade["sold"])
            total_invested += (trade_bought - trade_sold) * trade_coin
            total_bought += trade_bought - trade_sold

    profit_dict = {
        "earned_money": f"{Decimal(total_received) - Decimal(total_invested)}",
        "matecoin_account": f"{Decimal(total_bought) - Decimal(total_sold)}"
    }

    with open("profit.json", "w") as file:
        json.dump(profit_dict, file, indent=2)
