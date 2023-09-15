import decimal
import json


def calculate_profit(name_of_file: str) -> None:
    profit = 0
    amount_of_crypto = 0

    with open(name_of_file) as account_file:
        for account in json.load(account_file):
            if account["bought"] is None:
                amount_of_crypto -= decimal.Decimal(account["sold"])
                profit += (decimal.Decimal(account["sold"])
                           * decimal.Decimal(account["matecoin_price"]))
            elif account["sold"] is None:
                amount_of_crypto += decimal.Decimal(account["bought"])
                profit -= (decimal.Decimal(account["bought"])
                           * decimal.Decimal(account["matecoin_price"]))
            else:
                amount_of_crypto += (decimal.Decimal(account["bought"])
                                     - decimal.Decimal(account["sold"]))
                profit -= ((decimal.Decimal(account["bought"])
                            - decimal.Decimal(account["sold"]))
                           * decimal.Decimal(account["matecoin_price"]))
        result = {
            "earned_money": str(profit),
            "matecoin_account": str(amount_of_crypto)
        }
    with open("profit.json", "w") as profit_file:
        json.dump(result, profit_file, indent=2)
