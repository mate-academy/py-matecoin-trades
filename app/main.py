from decimal import Decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as source:
        transactions = json.load(source)
    coins_amount = Decimal(0)
    bought_in_dollars = Decimal(0)
    sold_in_dollars = Decimal(0)
    for day in transactions:
        matecoin_price = Decimal(day["matecoin_price"])
        if day["bought"] is not None:
            bought = Decimal(day["bought"])
            coins_amount += bought
            bought_in_dollars += bought * matecoin_price
        if day["sold"] is not None:
            sold = Decimal(day["sold"])
            coins_amount -= sold
            sold_in_dollars += sold * matecoin_price
    result = {
        "earned_money": str(sold_in_dollars - bought_in_dollars),
        "matecoin_account": str(coins_amount)
    }
    with open("profit.json", "w") as output:
        json.dump(result, output, indent=2)
