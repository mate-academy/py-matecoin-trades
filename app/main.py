import json
from decimal import Decimal


def calculate_profit(name: str):
    with open(name) as file_read:
        trades_data = json.load(file_read)
    money_dict = {}
    coin_account = Decimal("0")
    for trade in trades_data:
        if trade["sold"] is None:
            money_bought = Decimal(trade["bought"]) * \
                Decimal(trade["matecoin_price"])
            money_dict["bought"] = money_dict.get("bought", 0) + money_bought
            coin_account += Decimal(trade["bought"])
        if trade["bought"] is None:
            money_sold = Decimal(trade["sold"]) * \
                Decimal(trade["matecoin_price"])
            money_dict["sold"] = money_dict.get("sold", 0) + money_sold
            coin_account -= Decimal(trade["sold"])
    earned_money = money_dict["sold"] - money_dict["bought"]
    result = {"earned_money": str(earned_money),
              "matecoin_account": str(coin_account)}
    with open("profit.json", "w") as file_write:
        json.dump(result, file_write, indent=1)


if __name__ == '__main__':
    calculate_profit("trades.json")
