import json
from decimal import Decimal


def calculate_profit(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
    bought_sum = 0
    sold_sum = 0
    bought = 0
    sold = 0
    for wallet in data:
        if wallet['bought']:
            bought += Decimal(wallet['bought'])
            bought_sum += Decimal(
                wallet['bought']) * Decimal(wallet['matecoin_price'])
        if wallet['sold']:
            sold += Decimal(wallet['sold'])
            sold_sum += Decimal(
                wallet['sold']) * Decimal(wallet['matecoin_price'])
    earned_money = sold_sum - bought_sum
    matecoin_account = bought - sold
    total = {"earned_money": str(earned_money),
             "matecoin_account": str(matecoin_account)}
    with open('profit.json', 'w') as json_file:
        json.dump(total, json_file, indent=2)
