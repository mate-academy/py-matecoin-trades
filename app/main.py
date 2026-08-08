import json
import decimal


def calculate_profit(file_name: str) -> None:
    if file_name.split(".")[1] == "json":
        with open(file_name) as json_file:
            trades_data = json.load(json_file)

    earned_money = decimal.Decimal("0.0")
    matecoin_account = decimal.Decimal("0.0")

    for trade in trades_data:
        if not trade["bought"] is None:
            earned_money -= (decimal.Decimal(trade["bought"])
                             * decimal.Decimal(trade["matecoin_price"]))
            matecoin_account += decimal.Decimal(trade["bought"])
        if not trade["sold"] is None:
            earned_money += (decimal.Decimal(trade["sold"])
                             * decimal.Decimal(trade["matecoin_price"]))
            matecoin_account -= decimal.Decimal(trade["sold"])

    trades_result = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as result_file:
        json.dump(trades_result, result_file, indent=2)
