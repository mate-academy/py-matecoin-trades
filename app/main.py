import json
from decimal import Decimal


def calculate_profit(data: str) -> None:
    with open(data, "r") as json_file:
        date = json.load(json_file)

    total_earned_money = Decimal(0)
    matecoin_account = Decimal(0)
    total_spent = Decimal(0)

    for transaction in date:
        bought = transaction["bought"]
        sold = transaction["sold"]
        matecoin_price = Decimal(transaction["matecoin_price"])

        if bought:
            matecoin_account += Decimal(bought)
            total_spent += Decimal(bought) * matecoin_price

        if sold:
            matecoin_account -= Decimal(sold)
            earned_money = Decimal(sold) * matecoin_price
            total_earned_money += earned_money

    # Результат
    result = {
        "earned_money": str(total_earned_money - total_spent),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as result_file:
        json.dump(result, result_file, indent=2)
