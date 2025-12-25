import json
import decimal


def calculate_profit(json_file: str) -> None:

    coin_count = decimal.Decimal("0")
    earned_money = decimal.Decimal("0")

    with open(json_file, "r") as file:
        list_of_trades = json.load(file)

    for trade in list_of_trades:
        price = decimal.Decimal(trade["matecoin_price"])

        if trade["bought"] is not None:
            bought = decimal.Decimal(trade["bought"])
            coin_count += bought
            earned_money -= (price * bought)
            del bought

        if trade["sold"] is not None:
            sold = decimal.Decimal(trade["sold"])
            coin_count -= sold
            earned_money += (price * sold)
            del sold

        del price

    result_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(coin_count)}

    with open("profit.json", "w") as file:
        json.dump(result_dict, file, indent=2)


calculate_profit("app/trades.json")
