import json
import decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as trades_file:
        trades_list = json.load(trades_file)

    earned_money = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")

    for trade in trades_list:
        price = decimal.Decimal(trade["matecoin_price"])
        if trade["bought"] is not None:
            amount_bought = decimal.Decimal(trade["bought"])
            earned_money -= amount_bought * price
            matecoin_account += amount_bought

        if trade["sold"] is not None:
            amount_sold = decimal.Decimal(trade["sold"])
            earned_money += amount_sold * price
            matecoin_account -= amount_sold

    result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as profit_file:
        json.dump(result, profit_file, indent=2)
