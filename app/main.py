import sys
import json
from decimal import Decimal


try:
    file_name = sys.argv[1]
except IndexError:
    file_name = 'trades.json'


def calculate_profit(file_name):

    with open(file_name) as f:
        list_json = json.load(f)

    earned_money = 0
    matecoin_account = 0

    for coin in list_json:

        dec_matecoin_price = Decimal(coin["matecoin_price"])

        if coin['bought'] is None and coin['sold']:

            dec_sold = Decimal(coin['sold'])
            earned_money += dec_sold * dec_matecoin_price
            matecoin_account -= dec_sold

        elif coin['bought'] and coin['sold'] is None:

            dec_bought = Decimal(coin['bought'])
            earned_money -= dec_bought * dec_matecoin_price
            matecoin_account += dec_bought

        else:

            dec_bought = Decimal(coin['bought'])
            dec_sold = Decimal(coin['sold'])
            profit = dec_sold * dec_matecoin_price
            costs = dec_bought * dec_matecoin_price
            earned_money += profit - costs
            matecoin_account += dec_bought - dec_sold

    dict_profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(dict_profit, f, indent=2)
