import decimal
import json


def calculate_profit(name_of_json_file: str) -> None:
    with open(name_of_json_file) as trades_json:
        trades_file_in_python_code = json.load(trades_json)

    sum_of_profit = decimal.Decimal("0")
    sum_of_matecoin = decimal.Decimal("0")

    for trade in trades_file_in_python_code:
        if trade["bought"] is not None:
            sum_of_coins = decimal.Decimal(trade["bought"])
            price_of_coin = decimal.Decimal(trade["matecoin_price"])

            sum_of_profit -= sum_of_coins * price_of_coin
            sum_of_matecoin += decimal.Decimal(trade["bought"])

        if trade["sold"] is not None:
            sum_of_coins = decimal.Decimal(trade["sold"])
            price_of_coin = decimal.Decimal(trade["matecoin_price"])

            sum_of_profit += sum_of_coins * price_of_coin
            sum_of_matecoin -= decimal.Decimal(trade["sold"])

    with open("profit.json", "w") as profit_json:
        result = {
            "earned_money": str(sum_of_profit),
            "matecoin_account": str(sum_of_matecoin)
        }

        json.dump(result, profit_json, indent=2)
