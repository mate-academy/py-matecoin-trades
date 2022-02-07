import json


def calculate_profit(file_name):
    with open(file_name, mode='r') as fin:
        data = json.load(fin)

    profit = 0
    balance = 0
    for transaction in data:

        if transaction['sold'] is not None:
            profit += (float(transaction['sold'])
                       * float(transaction['matecoin_price']))
            balance -= float(transaction['sold'])
        elif transaction['bought'] is not None:
            profit -= (float(transaction['bought'])
                       * float(transaction['matecoin_price']))
            balance += float(transaction['bought'])

    with open('profit.json', mode='w') as fout:
        json.dump({'earned_money': profit, 'matecoin_account': balance}, fout)


calculate_profit('trades.json')
