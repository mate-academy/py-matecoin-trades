import json
from decimal import Decimal


def calculate_profit(trades_file):
    """
    Calculates profit from Matecoin trades, updates coin account,
    and saves the results to a JSON file.

    Args:
        trades_file (str): The name of the JSON file containing trade data.
    """

    try:
        with open(trades_file, 'r') as f:
            trades = json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{trades_file}' not found.")
        return
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in '{trades_file}'.")
        return

    matecoin_account = Decimal('0')
    earned_money = Decimal('0')

    for trade in trades:
        bought = trade.get('bought')
        sold = trade.get('sold')
        matecoin_price = trade.get('matecoin_price')

        if bought is not None:
            bought_amount = Decimal(str(bought))
            price = Decimal(str(matecoin_price))
            earned_money -= bought_amount * price
            matecoin_account += bought_amount
        elif sold is not None:
            sold_amount = Decimal(str(sold))
            price = Decimal(str(matecoin_price))
            earned_money += sold_amount * price
            matecoin_account -= sold_amount

    profit_data = {
        "earned_money": str(earned_money.quantize(Decimal("0.0000000"))),
        "matecoin_account": str(matecoin_account.quantize(Decimal("0.00000")))
    }

    try:
        with open('profit.json', 'w') as f:
            json.dump(profit_data, f, indent=2)
    except IOError as e:
        print(f"Error writing to 'profit.json': {e}")
        return
