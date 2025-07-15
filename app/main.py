import json
from decimal import Decimal

def calculate_profit(filename: str) -> None:
    with open(filename, 'r') as f:
        trades = json.load(f)

    earned_money = Decimal('0')
    matecoin_account = Decimal('0')

    for trade in trades:
        bought = trade.get('bought')
        sold = trade.get('sold')
        price = Decimal(trade['matecoin_price'])

        if bought is not None:
            amount_bought = Decimal(bought)
            matecoin_account += amount_bought
            earned_money -= amount_bought * price

        if sold is not None:
            amount_sold = Decimal(sold)
            matecoin_account -= amount_sold
            earned_money += amount_sold * price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open('profit.json', 'w') as f:
        json.dump(result, f)
