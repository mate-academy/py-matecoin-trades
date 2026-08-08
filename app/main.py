from decimal import Decimal
import json


def deserialize_from_json(trades_info_file_name: str):
    with open(trades_info_file_name, 'r') as trades_info_file:
        try:
            return json.loads(trades_info_file.read())
        except Exception as e:
            print(e)


def serialize_to_profit_file(
        earned_money,
        matecoin_account,
        profit_file_name="profit.json"
):
    with open(profit_file_name, 'w') as profit_file:
        try:
            json.dump(
                {
                    "earned_money": str(earned_money),
                    "matecoin_account": str(matecoin_account)
                },
                profit_file,
                indent=2
            )
        except Exception as e:
            print(e)


def calculate_profit(trades_info_file_name: str):
    trades = deserialize_from_json(trades_info_file_name)
    matecoin_account = 0
    earned_money = 0

    for trade in trades:
        if trade.get("bought"):
            matecoin_account += Decimal(trade["bought"])
            earned_money -= Decimal(trade["bought"]) * Decimal(trade["matecoin_price"])
        elif trade.get("sold"):
            matecoin_account -= Decimal(trade["sold"])
            earned_money += Decimal(trade["sold"]) * Decimal(trade["matecoin_price"])

    serialize_to_profit_file(earned_money, matecoin_account)


if __name__ == "__main__":
    calculate_profit('trades.json')
