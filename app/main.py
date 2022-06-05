import json

from decimal import Decimal


def calculate_profit(filename: str):

    earned_money = 0
    matecoin_account = 0

    with open(filename) as f:
        trades = json.load(f)

    for value in trades:

        if value['bought']:
            matecoin_account += Decimal(value['bought'])
            earned_money -= Decimal(value['bought'] * value['matecoin_price'])

        if value['sold']:
            matecoin_account -= Decimal(value['sold'])
            earned_money += Decimal(value['sold'] * value['matecoin_price'])

    with open('profit.json', 'w') as f:
        json.dump(
            {
                "earned_money": str(earned_money),
                "matecoin_account": str(matecoin_account)
            },
            f,
            indent=2
        )
