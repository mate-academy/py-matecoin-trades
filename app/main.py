from decimal import Decimal
import json


def calculate_profit(name_of_the_file: str) -> None:
    profit = 0
    coin_account = 0
    mc = "matecoin_price"
    with open(name_of_the_file) as f:
        trade_data = json.load(f)

        for tra in trade_data:
            if tra["bought"]:
                profit -= Decimal(tra["bought"]) * Decimal(tra[mc])
                coin_account += Decimal(tra["bought"])

            if tra["sold"]:
                profit += Decimal(tra["sold"]) * Decimal(tra[mc])
                coin_account -= Decimal(tra["sold"])

    profit_result = {
        "earned_money": str(profit),
        "matecoin_account": str(coin_account)
    }

    with open("profit.json", "w") as result_file:
        json.dump(profit_result, result_file, indent=2)
