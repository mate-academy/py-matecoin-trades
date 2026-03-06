import decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as trades_file:
        trades = json.load(trades_file)
        earnings = decimal.Decimal(0)
        matecoin_account = decimal.Decimal(0)
        for trade in trades:
            if trade["bought"] is None:
                bought = decimal.Decimal(0)
            else:
                bought = decimal.Decimal(trade["bought"])
            if trade["sold"] is None:
                sold = decimal.Decimal(0)
            else:
                sold = decimal.Decimal(trade["sold"])
            matecoin_price = decimal.Decimal(trade["matecoin_price"])
            earnings += sold * matecoin_price - bought * matecoin_price
            matecoin_account += (bought - sold)
    with open("profit.json", "w") as profit_file:
        data = {
            "earned_money": str(earnings),
            "matecoin_account": str(matecoin_account)
        }
        json.dump(data, profit_file, indent=2)
