import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:

    with open(filename, 'r') as data_file:
        trades = json.load(data_file)

    earned_money = Decimal("0")
    matecoin_account = Decimal("0")

    for trade in trades:
        bought = Decimal(trade.get('bought', 0) or 0)
        sold = Decimal(trade.get('sold', 0) or 0)
        matecoin_price = Decimal(trade['matecoin_price'])

        if bought > 0:
            matecoin_account += bought
            earned_money -= bought * matecoin_price
        elif sold > 0:
            matecoin_account -= bought
            earned_money += bought * matecoin_price

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as trade_result:
        json.dump(result, trade_result, indent=2)