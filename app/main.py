import decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades = json.load(file)

        earned_money = 0
        matecoin_account = 0
        profit = {}

        for transaction in trades:
            trade_volume = 0

            bought, sold, matecoin_price = transaction.values()

            if bought is not None:
                trade_volume -= decimal.Decimal(bought)
            if sold is not None:
                trade_volume += decimal.Decimal(sold)

            earned_money += trade_volume * decimal.Decimal(matecoin_price)
            matecoin_account += trade_volume

        profit["earned_money"] = str(earned_money)
        profit["matecoin_account"] = str(abs(matecoin_account))

    with open("profit.json", "w") as file:
        json.dump(profit, file, indent=2)
