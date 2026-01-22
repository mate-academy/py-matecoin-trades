import json
import decimal


def calculate_profit(file_name: str):

    with open(file_name, 'r') as f:
        trades = json.load(f)

    money_earned = decimal.Decimal(0)
    account = decimal.Decimal(0)

    for trade in trades:
        try:
            bought = decimal.Decimal(trade["bought"])
        except Exception:
            bought = decimal.Decimal("0")

        try:
            sold = decimal.Decimal(trade["sold"])
        except Exception:
            sold = decimal.Decimal("0")

        price = decimal.Decimal(trade["matecoin_price"])

        money_earned += (sold - bought) * price
        account += bought - sold

    with open("profit.json", "w") as f:
        json.dump({"earned_money": str(money_earned),
                   "matecoin_account": str(account)}, f, indent=2)
