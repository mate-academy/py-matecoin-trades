import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file_trades:
        trades = json.load(file_trades)
    sold_money = 0
    bought_money = 0
    sold = 0
    bought = 0
    for trade in trades:
        if trade["sold"] is not None:
            sold_money += (decimal.Decimal(trade["matecoin_price"])
                           * decimal.Decimal(trade["sold"]))
            sold += decimal.Decimal(trade["sold"])
        if trade["bought"] is not None:
            bought_money += (decimal.Decimal(trade["matecoin_price"])
                             * decimal.Decimal(trade["bought"]))
            bought += decimal.Decimal(trade["bought"])

    earned_money = decimal.Decimal(sold_money) - decimal.Decimal(bought_money)
    matecoin_account = decimal.Decimal(bought) - decimal.Decimal(sold)

    profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as file_profit:
        json.dump(profit, file_profit, indent=2)
