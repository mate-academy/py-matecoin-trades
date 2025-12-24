import json
import decimal


def calculate_profit(filename: str) -> None:
    with open(filename) as trade_file:
        trade_data = json.load(trade_file)

    matecoin_account = decimal.Decimal(0)
    earned_money = decimal.Decimal(0)

    for trade in trade_data:
        if trade["bought"] is not None:
            bought = decimal.Decimal(trade["bought"])
            matecoin_price = decimal.Decimal(trade["matecoin_price"])
            matecoin_account += bought
            earned_money -= bought * matecoin_price

        if trade["sold"] is not None:
            sold = decimal.Decimal(trade["sold"])
            matecoin_price = decimal.Decimal(trade["matecoin_price"])
            earned_money += sold * matecoin_price
            matecoin_account -= sold

    with open("profit.json", "w") as profit_json:
        done_data = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        json.dump(done_data, profit_json, indent=2)
