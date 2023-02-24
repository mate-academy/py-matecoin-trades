import json
import decimal


# write your code here


def calculate_profit(filename: str) -> None:
    transactions = json.load(open(filename))

    earned_money = decimal.Decimal()
    total_coins = decimal.Decimal()

    for transaction in transactions:
        earned_money -= decimal.Decimal(0 if transaction.get("bought") is None
                                        else transaction.get("bought")) \
            * decimal.Decimal(transaction.get("matecoin_price"))
        earned_money += decimal.Decimal(0 if transaction.get("sold") is None
                                        else transaction.get("sold")) \
            * decimal.Decimal(transaction.get("matecoin_price"))
        total_coins += decimal.Decimal(0 if transaction.get("bought") is None
                                       else transaction.get("bought")) \
            - decimal.Decimal(0 if transaction.get("sold") is None
                              else transaction.get("sold"))

    result_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(total_coins)
    }
    json.dump(result_dict, open("profit.json", "w"))
