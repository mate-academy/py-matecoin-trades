import json
from decimal import Decimal


def calculate_profit(filename: str) -> None:
    with open(filename, "r") as file:
        trades = json.load(file)
        earned_money = Decimal("0.0")
        matecoin_account = Decimal("0.0")
    for action in trades:
        bought = action["bought"]
        sold = action["sold"]
        price = Decimal(action["matecoin_price"])
        if bought is not None:
            coin = Decimal(bought)
            delta = price * coin
            earned_money -= delta
            matecoin_account += coin
        if sold is not None:
            coin = Decimal(sold)
            delta = price * coin
            earned_money += delta
            matecoin_account -= coin
    result = {
        "earned_money": earned_money.to_eng_string(),
        "matecoin_account": matecoin_account.to_eng_string()
    }
    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
