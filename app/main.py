from decimal import Decimal
import json


def calculate_profit(file_name):
    amount_of_fiat = 0
    amount_of_coins = 0
    with open(file_name, "r") as source_json:
        data_trades = json.load(source_json)
        for trade in data_trades:
            coin_price = Decimal(trade["matecoin_price"])
            if trade["bought"]:
                amount_of_fiat -= Decimal(trade["bought"]) * coin_price
                amount_of_coins += Decimal(trade["bought"])
            elif trade["sold"]:
                amount_of_fiat += Decimal(trade["sold"]) * coin_price
                amount_of_coins -= Decimal(trade["sold"])
    profit_and_loss = {
        "earned_money": str(amount_of_fiat),
        "matecoin_account": str(amount_of_coins)
    }
    with open("profit.json", "w") as profit_report:
        json.dump(profit_and_loss, profit_report, indent=2)


if __name__ == '__main__':
    calculate_profit("trades.json")
