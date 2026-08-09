import json
import decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        data = json.load(file)

    coin_count = decimal.Decimal("0")
    total_profit = decimal.Decimal("0")

    for item in data:
        price = decimal.Decimal(item["matecoin_price"])

        if item.get("bought"):
            bought = decimal.Decimal(item["bought"])
            coin_count += bought
            total_profit -= bought * price

        if item.get("sold"):
            sold = decimal.Decimal(item["sold"])
            coin_count -= sold
            total_profit += sold * price

    with open("profit.json", "w") as file:
        json.dump(
            {
                "earned_money": str(total_profit),
                "matecoin_account": str(coin_count),
            },
            file,
            indent=2,
        )
