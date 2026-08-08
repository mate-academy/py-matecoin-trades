import json
import decimal


def calculate_profit(trades_data_file: str) -> None:

    with open(trades_data_file) as input_data_file, \
            open("profit.json", "w") as profit_file:

        trades_data = json.load(input_data_file)

        bought_total = 0
        bought_value = 0
        sold_total = 0
        sold_value = 0

        for trade in trades_data:

            if trade["bought"] is not None:
                bought_total += decimal.Decimal(f'{trade["bought"]}')
                bought_value += decimal.Decimal(f'{trade["bought"]}') * \
                    decimal.Decimal(f'{trade["matecoin_price"]}')

            if trade["sold"] is not None:
                sold_total += decimal.Decimal(f'{trade["sold"]}')
                sold_value += decimal.Decimal(f'{trade["sold"]}') * \
                    decimal.Decimal(f'{trade["matecoin_price"]}')

        matecoin_account = str(decimal.Decimal(f"{bought_total}")
                               - decimal.Decimal(f"{sold_total}"))
        earned_money = str(decimal.Decimal(f"{sold_value}")
                           - decimal.Decimal(f"{bought_value}"))
        profit = {"earned_money": earned_money,
                  "matecoin_account": matecoin_account}

        json.dump(profit, profit_file, indent=2)
