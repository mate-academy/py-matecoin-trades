import decimal
import json


def calculate_profit(trades_filename: str) -> None:
    with open(trades_filename, "rt") as trades_file:
        trades = json.load(trades_file)

    result = {
        "earned_money": decimal.Decimal("0.0"),
        "matecoin_account": decimal.Decimal("0.0")
    }

    for deal in trades:
        earned_money = decimal.Decimal("0.0")
        matecoin_account = decimal.Decimal("0.0")
        if deal["bought"] is not None:
            earned_money -= \
                decimal.Decimal(deal["bought"]) * \
                decimal.Decimal(deal["matecoin_price"])
            matecoin_account += decimal.Decimal(deal["bought"])
        if deal["sold"] is not None:
            earned_money += \
                decimal.Decimal(deal["sold"]) * \
                decimal.Decimal(deal["matecoin_price"])
            matecoin_account -= decimal.Decimal(deal["sold"])

        result["earned_money"] = \
            result["earned_money"] + earned_money
        result["matecoin_account"] = \
            result["matecoin_account"] + matecoin_account

    for key, value in result.items():
        result[key] = f"{result[key]}"

    result_filename = "profit.json"
    with open(result_filename, "wt") as result_file:
        json.dump(result, result_file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
