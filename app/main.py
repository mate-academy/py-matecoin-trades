import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trades_data = json.load(file)

        money_spent = Decimal(0)
        money_received = Decimal(0)
        total_bought = Decimal(0)
        total_sold = Decimal(0)

        for transaction in trades_data:
            matecoin_price = Decimal(transaction["matecoin_price"])
            if transaction["bought"] is not None:
                bought_amount = Decimal(transaction["bought"])
                total_bought += bought_amount
                money_spent += bought_amount * matecoin_price
            if transaction["sold"] is not None:
                sold_amount = Decimal(transaction["sold"])
                total_sold += sold_amount
                money_received += sold_amount * matecoin_price
            matecount_account = total_bought - total_sold
            earned_money = money_received - money_spent
        profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecount_account)
        }
        with open("profit.json", "w") as result_file:
            json.dump(profit, result_file, indent=2)
