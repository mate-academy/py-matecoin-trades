import json
import decimal


def calculate_profit(name: json) -> None:
    with open(name, "r") as f:
        trades = json.load(f)

    decimal_money = decimal.Decimal("0")
    decimal_mat_account = decimal.Decimal("0")

    for trade in trades:
        if trade["bought"] is not None:
            decimal_bought = decimal.Decimal(trade["bought"])
            decimal_mt_price = decimal.Decimal(trade["matecoin_price"])
            decimal_mat_account += decimal_bought
            decimal_money -= decimal_bought * decimal_mt_price
        if trade["sold"] is not None:
            decimal_sold = decimal.Decimal(trade["sold"])
            decimal_mt_price = decimal.Decimal(trade["matecoin_price"])
            decimal_mat_account -= decimal_sold
            decimal_money += decimal_sold * decimal_mt_price

    profit = {
        "earned_money": str(decimal_money),
        "matecoin_account": str(decimal_mat_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit, f, indent=2)
