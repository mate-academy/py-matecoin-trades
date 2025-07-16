import json
import decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r", encoding="UTF-8") as file:
        trades = json.load(file)

    profit = decimal.Decimal("0.0")
    account = decimal.Decimal("0.0")

    for trade in trades:
        if trade["bought"]:
            bought = decimal.Decimal(trade["bought"])
            profit -= bought * decimal.Decimal(trade["matecoin_price"])
            account += bought

        if trade["sold"]:
            sold = decimal.Decimal(trade["sold"])
            profit += sold * decimal.Decimal(trade["matecoin_price"])
            account -= sold

    result = {
        "earned_money": str(profit),
        "matecoin_account": str(account)
    }

    with open("profit.json", "w", encoding="UTF-8") as file:
        json.dump(result, file, indent=2)
