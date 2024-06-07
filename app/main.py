from decimal import Decimal
import json


def calculate_profit(file_name):
    with open(file_name, 'r') as f:
        trades = json.load(f)

    total_bought = Decimal('0.0')
    total_sold = Decimal('0.0')
    earned_money = Decimal('0.0')

    for trade in trades:
        bought_str = trade.get('bought')
        sold_str = trade.get('sold')
        price_str = trade.get('matecoin_price')

        if bought_str:
            total_bought += Decimal(bought_str)
        if sold_str:
            total_sold += Decimal(sold_str)
            earned_money += Decimal(sold_str) * Decimal(price_str)

        matecoin_account = total_bought - total_sold

        profit_data = {
          'earned_money': str(earned_money - total_bought * Decimal(price_str)),
          'matecoin_account': str(matecoin_account)
        }

    with open('profit.json', 'w') as f:
        json.dump(profit_data, f, indent=4)
