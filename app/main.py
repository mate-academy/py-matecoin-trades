import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as j_file:
        data_base = json.load(j_file)
    coin_account = 0
    spend_money = 0
    for transaction in data_base:
        price_coin = Decimal(transaction["matecoin_price"])
        if transaction["bought"] is not None:
            coin_bought = Decimal(transaction["bought"])
            spend_money = spend_money - price_coin * coin_bought
            coin_account = coin_account + coin_bought
        if transaction["sold"] is not None:
            coin_sold = Decimal(transaction["sold"])
            spend_money = spend_money + price_coin * coin_sold
            coin_account = coin_account - coin_sold
    output = {
        "earned_money": str(spend_money),
        "matecoin_account": str(coin_account)
    }
    with open("profit.json", "w") as output_file:
        json.dump(output, output_file, indent=2)
