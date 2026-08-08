import json
import decimal


def calculate_profit(filename: str = "trades.json") -> None:

    with open(filename, "r") as f:
        trades = json.load(f)

        matecoin_account = 0
        earned_money = 0
        for trade in trades:
            if trade["bought"] is None:
                trade["bought"] = 0
            if trade["sold"] is None:
                trade["sold"] = 0
            bought = decimal.Decimal(str(trade["bought"]))
            sold = decimal.Decimal(str(trade["sold"]))
            matecoin_account += bought - sold
            matecoin_price = decimal.Decimal(str(trade["matecoin_price"]))
            earned_money += sold * matecoin_price - bought * matecoin_price
            decimal_earned = decimal.Decimal(str(earned_money))

        result = {"earned_money": str(decimal_earned),
                  "matecoin_account": str(matecoin_account)}

        with open("profit.json", "w") as f:
            json.dump(result, f, indent=2)
