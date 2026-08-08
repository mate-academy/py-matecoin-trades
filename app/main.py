import json
from decimal import Decimal


def calculate_profit(name: str):
    with open(name) as file_read:
        trades_data = json.load(file_read)
    money_account = Decimal("0")
    coin_account = Decimal("0")
    for trade in trades_data:
        if trade["bought"]:
            money_account -= Decimal(trade["bought"]) * \
                Decimal(trade["matecoin_price"])
            coin_account += Decimal(trade["bought"])
        if trade["sold"]:
            money_account += Decimal(trade["sold"]) * \
                Decimal(trade["matecoin_price"])
            coin_account -= Decimal(trade["sold"])
    result = {"earned_money": str(money_account),
              "matecoin_account": str(coin_account)}
    with open("profit.json", "w") as file_write:
        json.dump(result, file_write, indent=1)


if __name__ == '__main__':
    calculate_profit("trades.json")
