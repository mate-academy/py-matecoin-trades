import json
import decimal


def calculate_profit(file_name: str) -> None:
    earned_money = 0
    matecoin_account = 0

    with open(file_name) as f:
        trades_data = json.load(f)

    for trade in trades_data:
        price = decimal.Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = decimal.Decimal(trade["bought"])

            matecoin_account += bought
            earned_money -= bought * price
        if trade["sold"] is not None:
            sold = decimal.Decimal(trade["sold"])

            matecoin_account -= sold
            earned_money += sold * price

    result_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f2:
        json.dump(result_data, f2, indent=2)
