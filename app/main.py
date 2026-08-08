import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    with open(name_file, 'r') as trades_file:
        trades_file = json.load(trades_file)

    buy_matecoin = 0
    sell_matecoin = 0
    matecoin_account = 0

    for item in trades_file:
        price_matecoin = Decimal(item["matecoin_price"])
        if item['bought'] is not None:
            data_bought = Decimal(item["bought"])
            buy_matecoin += data_bought * price_matecoin
            matecoin_account += data_bought
        if item['sold'] is not None:
            data_sold = Decimal(item["sold"])
            sell_matecoin += data_sold * price_matecoin
            matecoin_account -= data_sold

    result_profit = {
        "earned_money": str(sell_matecoin - buy_matecoin),
        "matecoin_account": str(matecoin_account)
    }

    with open("profit.json", 'w') as file_profit:
        json.dump(result_profit, file_profit, indent=2)


if __name__ == "__main__":
    calculate_profit('trades.json')
