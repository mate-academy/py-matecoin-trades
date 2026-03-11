import decimal
import json


def calculate_profit(filename: str) -> None:
    result = {}
    with (open(filename, "r") as json_file):
        data = json.load(json_file)

        for trade in data:
            if trade["bought"] is None:
                trade["bought"] = 0

            if trade["sold"] is None:
                trade["sold"] = 0

            matecoin_price_decimal = decimal.Decimal(trade["matecoin_price"])
            bought_decimal = decimal.Decimal(trade["bought"])
            sold_decimal = decimal.Decimal(trade["sold"])

            result["earned_money"] = (result.get("earned_money", 0)
                                      + sold_decimal * matecoin_price_decimal
                                      - bought_decimal
                                      * matecoin_price_decimal)

            result["matecoin_account"] = (result.get("matecoin_account", 0)
                                          + bought_decimal - sold_decimal)

    with open("profit.json", "w") as json_file:
        result["earned_money"] = str(result["earned_money"])
        result["matecoin_account"] = str(result["matecoin_account"])

        json.dump(result, json_file, indent=2)
