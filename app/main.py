import json
import decimal


def calculate_profit(file_name: str) -> None:

    with open(file_name, "r") as file:
        data = json.load(file)

    money_spent = decimal.Decimal("0.0")
    money_earned = decimal.Decimal("0.0")
    crypto = decimal.Decimal("0.0")

    for trade in data:
        if trade["bought"]:
            bought_amount = decimal.Decimal(trade["bought"])
            matecoin_price = decimal.Decimal(trade["matecoin_price"])
            crypto += bought_amount
            money_spent += bought_amount * matecoin_price

        if trade["sold"]:
            sold_amount = decimal.Decimal(trade["sold"])
            matecoin_price = decimal.Decimal(trade["matecoin_price"])
            crypto -= sold_amount
            money_earned += sold_amount * matecoin_price

    result = {
        "earned_money": str(money_earned - money_spent),
        "matecoin_account": str(crypto)
    }

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)
