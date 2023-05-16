from decimal import Decimal
import json


def calculate_profit(name_file: str) -> None:
    with (
        open(name_file) as file,
        open("profit.json", "w") as profit_file
    ):

        transaction_data = json.load(file)

        earned_money = 0
        matecoin_account = 0

        for transaction in transaction_data:

            dec_bought = Decimal(transaction.get("bought")) if (
                transaction.get("bought")
            ) else 0
            dec_sold = Decimal(transaction.get("sold")) if (
                transaction.get("sold")
            ) else 0

            dec_mate_price = Decimal(transaction.get("matecoin_price"))
            earned_money += (
                dec_sold
                * dec_mate_price
                - dec_bought
                * dec_mate_price
            )
            matecoin_account += dec_bought - dec_sold

        ended_profit = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        json.dump(ended_profit, profit_file, indent=2)
