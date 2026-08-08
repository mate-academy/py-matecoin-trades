import decimal
import json


def calculate_profit(input_file: json) -> None:
    with open(input_file) as input_file:
        trades_data = json.load(input_file)
    spent_money = 0
    bought = 0
    earned_money = 0
    sold = 0
    for item in trades_data:
        if item["bought"] is not None:
            spent_money += (decimal.Decimal(item["bought"])
                            * decimal.Decimal(item["matecoin_price"]))
            bought += decimal.Decimal(item["bought"])
        if item["sold"] is not None:
            earned_money += (decimal.Decimal(item["sold"])
                             * decimal.Decimal(item["matecoin_price"]))
            sold += decimal.Decimal(item["sold"])

    trade_results = {
        "earned_money": str(earned_money - spent_money),
        "matecoin_account": str(bought - sold)
    }
    with open("profit.json", "w") as profit:
        json.dump(trade_results, profit, indent=2)
