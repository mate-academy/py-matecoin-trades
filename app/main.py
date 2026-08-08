import json
import decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)
    total = decimal.Decimal("0")
    matecoin_account = decimal.Decimal("0")
    for item in trades:
        matecoin_price = decimal.Decimal(item["matecoin_price"])
        if item["bought"]:
            bought = decimal.Decimal(item["bought"])
            matecoin_account += bought
            total -= bought * matecoin_price
        if item["sold"]:
            sold = decimal.Decimal(item["sold"])
            matecoin_account -= decimal.Decimal(sold)
            total += sold * matecoin_price

    result = {
        "earned_money": str(total),
        "matecoin_account": str(matecoin_account)
    }
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
