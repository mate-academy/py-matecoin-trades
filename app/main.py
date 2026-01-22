import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        my_trades = json.load(file)
        current_coins = 0
        bucks = 0
        for elem in my_trades:
            dec_rate = Decimal(elem["matecoin_price"])
            if elem["bought"] is not None:
                dec_bought = Decimal(elem["bought"])
                current_coins += dec_bought
                bucks -= dec_bought * dec_rate
            if elem["sold"] is not None:
                dec_sold = Decimal(elem["sold"])
                current_coins -= dec_sold
                bucks += dec_sold * dec_rate
    result = {"earned_money": str(bucks),
              "matecoin_account": str(current_coins)}
    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
