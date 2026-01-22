import json
import decimal


def calculate_profit(file_with_trades_info: str):
    with open(file_with_trades_info) as f_out, \
            open("profit.json", "w") as f_in:
        trades_info = json.load(f_out)
        earned_money = decimal.Decimal("0.0")
        matecoin_account = decimal.Decimal("0.0")
        for trade in trades_info:
            price = decimal.Decimal(trade['matecoin_price'])
            if trade['bought'] is not None:
                earned_money -= decimal.Decimal(trade['bought']) * price
                matecoin_account += decimal.Decimal(trade['bought'])
            if trade['sold'] is not None:
                earned_money += decimal.Decimal(trade['sold']) * price
                matecoin_account -= decimal.Decimal(trade['sold'])

        json.dump({
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }, f_in, indent=2)
