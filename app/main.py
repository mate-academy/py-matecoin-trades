from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as trade_file:
        trades = json.load(trade_file)

        money_bilance = Decimal()
        matecoin_bilace = Decimal()
        for trade in trades:
            matecoin_price = Decimal(trade["matecoin_price"])
            if trade["sold"] is not None:
                income = Decimal(trade["sold"]) * matecoin_price
                money_bilance += income
                matecoin_bilace -= Decimal(trade["sold"])
            if trade["bought"] is not None:
                expense = Decimal(trade["bought"]) * matecoin_price
                money_bilance -= expense
                matecoin_bilace += Decimal(trade["bought"])

        bilance = {
            "earned_money": str(money_bilance),
            "matecoin_account": str(matecoin_bilace)
        }

        with open("profit.json", "w") as bilance_file:
            json.dump(bilance, bilance_file, indent=2)
