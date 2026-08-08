import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as file:
        profit = {"earned_money": 0, "matecoin_account": 0}
        trades = json.load(file)
        for trade in trades:
            mate_price = Decimal(trade['matecoin_price'])
            if trade['bought']:
                profit['earned_money'] -= Decimal(trade['bought']) * mate_price
                profit['matecoin_account'] += Decimal(trade['bought'])
            if trade['sold']:
                profit['earned_money'] += Decimal(trade['sold']) * mate_price
                profit['matecoin_account'] -= Decimal(trade['sold'])
    with open("profit.json", "w") as file:
        profit['earned_money'] = f"{profit['earned_money']}"
        profit['matecoin_account'] = f"{profit['matecoin_account']}"
        json.dump(profit, file, indent=2)
