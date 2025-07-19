import json
from decimal import Decimal, getcontext


def calculate_profit(filename):
    getcontext().prec = 28

    with open(filename, 'r') as f:
        trades = json.load(f)

    earned_money = Decimal('0')
    matecoin_account = Decimal('0')

    for trade in trades:
        price = Decimal(trade['matecoin_price'])

        if trade['bought']:
            bought = Decimal(trade['bought'])
            earned_money -= bought * price
            matecoin_account += bought

        if trade['sold']:
            sold = Decimal(trade['sold'])
            earned_money += sold * price
            matecoin_account -= sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2)
