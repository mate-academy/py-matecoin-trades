import decimal
import json


def calculate_profit(name_file: str) -> None:
    with open(name_file, "r") as file:
        json_open = json.load(file)

    earn_money = 0
    coin_account = 0

    for name in json_open:
        if name["bought"] is not None:
            coin_account += decimal.Decimal(name["bought"])
            earn_money -= \
                decimal.Decimal(name["bought"]) * \
                decimal.Decimal(name["matecoin_price"])
        if name["sold"] is not None:
            coin_account -= decimal.Decimal(name["sold"])
            earn_money += \
                decimal.Decimal(name["sold"]) * \
                decimal.Decimal(name["matecoin_price"])

    profit_json = {
        "earned_money": str(earn_money),
        "matecoin_account": str(coin_account)}

    with open("profit.json", "w") as file:
        json.dump(profit_json, file, indent=2)
