import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        info = json.load(file)

    earned_money = decimal.Decimal("0")
    coin_count = decimal.Decimal("0")

    for deal in info:
        if deal["bought"] is not None:
            bought_decimal = decimal.Decimal(deal["bought"])
            coin_decimal = decimal.Decimal(deal["matecoin_price"])
            coin_count += bought_decimal
            earned_money = earned_money - bought_decimal * coin_decimal

        if deal["sold"] is not None:
            sold_decimal = decimal.Decimal(deal["sold"])
            coin_decimal = decimal.Decimal(deal["matecoin_price"])
            coin_count -= sold_decimal
            earned_money = earned_money + sold_decimal * coin_decimal
    str_earned_money = str(earned_money)
    str_coin_count = str(coin_count)
    profit = {
        "earned_money": str_earned_money,
        "matecoin_account": str_coin_count
    }
    with open("profit.json", "w") as profit_file:
        json.dump(profit, profit_file, indent=2)
