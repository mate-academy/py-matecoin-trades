import decimal
import json


def calculate_profit(trades_information_file: json) -> None:
    money_bought = []
    money_sold = []
    coin_bought = []
    coin_sold = []
    profit_data = {}
    with open(trades_information_file, "r") as f:
        statistic_data = json.load(f)
        for trades in statistic_data:
            matecoin_price = decimal.Decimal(trades["matecoin_price"])
            if trades["bought"]:
                bought = decimal.Decimal(trades["bought"])
                money_bought.append(bought * matecoin_price)
                coin_bought.append(bought)
            if trades["sold"]:
                sold = decimal.Decimal(trades["sold"])
                money_sold.append(sold * matecoin_price)
                coin_sold.append(sold)
    earned_money = sum(money_sold) - sum(money_bought)
    matecoin_account = sum(coin_bought) - sum(coin_sold)
    profit_data["earned_money"] = str(earned_money)
    profit_data["matecoin_account"] = str(matecoin_account)
    with open("profit.json", "w") as f:
        json.dump(profit_data, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
