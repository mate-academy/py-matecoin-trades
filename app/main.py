import json
import decimal


def calculate_profit(file_name: str = "trades.json") -> None:
    with open(file_name) as f:
        transactions = json.load(f)

    spend_dollar = 0
    bought_coin = 0
    received_dollar = 0
    sold_coin = 0

    for transact in transactions:
        if transact["bought"]:
            spend_dollar += decimal.Decimal(transact["bought"]) \
                * decimal.Decimal(transact["matecoin_price"])
            bought_coin += decimal.Decimal(transact["bought"])

        if transact["sold"]:
            received_dollar += decimal.Decimal(transact["sold"]) \
                * decimal.Decimal(transact["matecoin_price"])
            sold_coin += decimal.Decimal(transact["sold"])

    earned_money = received_dollar - spend_dollar
    matecoin_account = bought_coin - sold_coin
    profit_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", "w") as f:
        json.dump(profit_dict, f, indent=2)
