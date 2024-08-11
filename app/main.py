import decimal
import json


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        data = json.load(file)
        print(data)

        bought_crypto = 0
        sold_crypto = 0
        bought_coins = 0
        sold_coins = 0
        for el in data:
            price = decimal.Decimal(el["matecoin_price"])
            if el["bought"]:
                bought = decimal.Decimal(el["bought"])
                bought_coins += bought
                bought_crypto += bought * price
            if el["sold"]:
                sold = decimal.Decimal(el["sold"])
                sold_coins += sold
                sold_crypto += sold * price

        treads = {
            "earned_money": str(sold_crypto - bought_crypto),
            "matecoin_account": str(bought_coins - sold_coins)
        }

    with open("profit.json", "w") as f:
        json.dump(treads, f, indent=2)
