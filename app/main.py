import json
import decimal


def calculate_profit(name_file: str) -> None:
    with open(name_file) as open_file:
        trades_data = json.load(open_file)

    profit_matecoin = 0
    profit_earned = 0

    for data in trades_data:

        if data["bought"] is not None:
            profit_matecoin += decimal.Decimal(data["bought"])
            profit_earned -= decimal.Decimal(data["bought"]) \
                * decimal.Decimal(data["matecoin_price"])

        if data["sold"] is not None:
            profit_matecoin -= decimal.Decimal(data["sold"])
            profit_earned += decimal.Decimal(data["sold"]) \
                * decimal.Decimal(data["matecoin_price"])

    profit_data = {"earned_money": str(profit_earned),
                   "matecoin_account": str(profit_matecoin)}

    with open("profit.json", "w") as profit:
        json.dump(profit_data, profit, indent=2)
