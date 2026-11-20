import json
import decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as read_file:
        trades = json.load(read_file)

    earned_money = decimal.Decimal(0)
    matecoin_account = decimal.Decimal(0)
    for trade in trades:
        price_decimal = decimal.Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought_decimal = decimal.Decimal(trade["bought"])
            earned_money -= bought_decimal * price_decimal
            matecoin_account += bought_decimal
        if trade["sold"] is not None:
            sold_decimal = decimal.Decimal(trade["sold"])
            earned_money += sold_decimal * price_decimal
            matecoin_account -= sold_decimal

    earned_money_str = str(earned_money)
    matecoin_account_str = str(matecoin_account)

    result = {
        "earned_money": earned_money_str,
        "matecoin_account": matecoin_account_str
    }

    with open("profit.json", "w") as write_file:
        json.dump(result, write_file, indent=2)
