import json
from decimal import Decimal

def calculate_profit(filename):
    # 1. Load the data from the json file
    with open(filename, 'r') as file:
        trades = json.load(file)

    # Initialize balances using Decimal
    earned_money = Decimal('0')
    matecoin_account = Decimal('0')

    # 2. Iterate through each trade and update balances
    for trade in trades:
        # Convert price to Decimal immediately
        price = Decimal(trade['matecoin_price'])

        # Logic for Buying
        if trade['bought'] is not None:
            volume = Decimal(trade['bought'])
            # Spending money (negative) to get coins (positive)
            earned_money -= volume * price
            matecoin_account += volume

        # Logic for Selling
        if trade['sold'] is not None:
            volume = Decimal(trade['sold'])
            # Gaining money (positive) by giving away coins (negative)
            earned_money += volume * price
            matecoin_account -= volume

    # 3. Prepare the final data structure
    # We convert Decimals to strings as requested
    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    # 4. Dump the data into profit.json
    with open('profit.json', 'w') as outfile:
        json.dump(result, outfile)
