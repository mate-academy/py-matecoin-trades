import json
import decimal


def calculate_profit(trades: json) -> None:

    bought_money = decimal.Decimal(0)
    sold_money = decimal.Decimal(0)

    matecoin_account_bought = decimal.Decimal(0)
    matecoin_account_sold = decimal.Decimal(0)

    with open(trades) as file:
        trades_data = json.load(file)

    for key in trades_data:
        if key["bought"] and not isinstance(key["sold"], str):
            dec_bought_number = decimal.Decimal(key["bought"])
            dec_price = decimal.Decimal(key["matecoin_price"])
            bought_money += dec_bought_number
            matecoin_account_bought += (dec_bought_number * dec_price)

        elif key["sold"] and not isinstance(key["bought"], str):
            dec_sold_number = decimal.Decimal(key["sold"])
            dec_price = decimal.Decimal(key["matecoin_price"])
            sold_money += dec_sold_number
            matecoin_account_sold += (dec_sold_number * dec_price)

        else:
            dec_bought_number = decimal.Decimal(key["bought"])
            dec_sold_number = decimal.Decimal(key["sold"])
            bought_money += dec_bought_number
            sold_money += dec_sold_number

            dec_price = decimal.Decimal(key["matecoin_price"])
            matecoin_account_bought += (dec_bought_number * dec_price)
            matecoin_account_sold += (dec_sold_number * dec_price)

    matecoin_account = (matecoin_account_sold - matecoin_account_bought)
    earned_money = (bought_money - sold_money)

    profit_dict = {"earned_money": str(matecoin_account),
                   "matecoin_account": str(earned_money)}

    with open("/Users/sergey/meta_project/py-matecoin-trades/profit.json", "w") as file:
        json.dump(profit_dict, file, indent=2)
