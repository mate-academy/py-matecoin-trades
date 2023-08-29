import json
import decimal


def calculate_profit(
        trades_file: str = "trades.json",
        profit_file: str = "profit.json"
) -> None:
    with open(trades_file, "r") as work_file:
        work_data = json.load(work_file)

    sum_bought = 0
    sum_sold = 0
    sum_matecoit = 0
    for data in work_data:
        if data["bought"] is not None:
            sum_bought += (
                decimal.Decimal(data["bought"])
                * decimal.Decimal(data["matecoin_price"])
            )
            sum_matecoit += decimal.Decimal(data["bought"])
        if data["sold"] is not None:
            sum_sold += (
                decimal.Decimal(data["sold"])
                * decimal.Decimal(data["matecoin_price"])
            )
            sum_matecoit -= decimal.Decimal(data["sold"])
    earned_money = sum_sold - sum_bought
    dict_profit = {
        "earned_money": str(earned_money),
        "matecoin_account": str(sum_matecoit)
    }

    with open(profit_file, "w") as result_file:
        json.dump(dict_profit, result_file, indent=2)