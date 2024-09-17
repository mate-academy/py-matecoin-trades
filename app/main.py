from decimal import Decimal
import json


def calculate_profit(file_name: str):
    earned_money = 0
    matecoin_account = 0

    with open(file_name, "r") as trades, \
            open("profit.json", "w") as profit_json:
        deals = json.load(trades)

        for deal in deals:

            if deal["bought"] is not None:
                spend_money = Decimal(deal["bought"]) \
                    * Decimal(deal["matecoin_price"])
                earned_money -= spend_money
                matecoin_account += Decimal(deal["bought"])

            if deal["sold"] is not None:
                earn_money = Decimal(deal["sold"]) \
                    * Decimal(deal["matecoin_price"])
                earned_money += earn_money
                matecoin_account -= Decimal(deal["sold"])

        account_status = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        json.dump(account_status, profit_json, indent=2)
