import json
from decimal import Decimal, getcontext
from typing import List, Dict

getcontext().prec = 28


def calculate_profit(trades_filename: str) -> None:
    earned_money = Decimal('0')
    matecoin_account = Decimal('0')

    try:
        with open(trades_filename, 'r', encoding='utf-8') as f:
            trades: List[Dict] = json.load(f)
    except Exception:
        return

    for trade in trades:
        price = Decimal(trade['matecoin_price'])
        if trade['bought'] is not None:
            bought_volume = Decimal(trade['bought'])

            matecoin_account += bought_volume
            earned_money -= bought_volume * price

        if trade['sold'] is not None:
            sold_volume = Decimal(trade['sold'])

            matecoin_account -= sold_volume
            earned_money += sold_volume * price
    matecoin_result = matecoin_account.quantize(Decimal('0.00001'))
    earned_result = earned_money.quantize(Decimal('0.0000001'))

    profit_data = {
        "earned_money": str(earned_result),
        "matecoin_account": str(matecoin_result)
    }

    output_filename = "profit.json"

    try:
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(profit_data, f, indent=2)
    except Exception:
        return

    return None
