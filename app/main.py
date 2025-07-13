import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name) as trade_file_info:
        trade_info = json.load(trade_file_info)

    earned_money = decimal.Decimal("0.0")
    matecoin_account = decimal.Decimal("0.0")

    for operation in trade_info:
        currency = decimal.Decimal(operation["matecoin_price"])
        bought_coins = decimal.Decimal("0.0")
        if operation["bought"] is not None:
            bought_coins = decimal.Decimal(operation["bought"])
        sold_coins = decimal.Decimal("0.0")
        if operation["sold"] is not None:
            sold_coins = decimal.Decimal(operation["sold"])
        earned_money += (sold_coins * currency) + (-bought_coins * currency)
        matecoin_account += -sold_coins + bought_coins

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account),
    }

    with open("profit.json", "w") as profit_data_file:
        json.dump(profit_data, profit_data_file, indent=2)
