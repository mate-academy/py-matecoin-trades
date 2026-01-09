import json
import decimal


def calculate_profit(filename: str) -> None:
    with open(filename) as f:
        trades = json.load(f)
        print(trades)

    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")
    for trade in trades:
        if trade["bought"] is not None:
            bought_amount = decimal.Decimal(trade["bought"])
            price = decimal.Decimal(trade["matecoin_price"])
            matecoin_account += bought_amount
            earned_money -= bought_amount * price
        if trade["sold"] is not None:
            sold_amount = decimal.Decimal(trade["sold"])
            price = decimal.Decimal(trade["matecoin_price"])
            matecoin_account -= sold_amount
            earned_money += sold_amount * price
    earned_money = str(earned_money)
    matecoin_account = str(matecoin_account)

    result = {
        "matecoin_account": matecoin_account,
        "earned_money": earned_money,
    }
    with open("profit.json", "w") as f:
        json.dump(result, f, indent=2, sort_keys=True)
