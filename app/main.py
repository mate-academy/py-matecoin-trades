import json
import decimal


def calculate_profit(trades_file: str) -> None:
    profit = decimal.Decimal(0)
    coin_account = decimal.Decimal(0)

    with open(trades_file, "r") as file:
        trades = json.load(file)

    for trade in trades:
        if trade["bought"] is not None:
            bought = decimal.Decimal(trade["bought"])
            matecoin_price = decimal.Decimal(trade["matecoin_price"])
            profit -= (bought * matecoin_price)
            coin_account += bought
        if trade["sold"] is not None:
            sold = decimal.Decimal(trade["sold"])
            matecoin_price = decimal.Decimal(trade["matecoin_price"])
            profit += (sold * matecoin_price)
            coin_account -= sold

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(coin_account)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
