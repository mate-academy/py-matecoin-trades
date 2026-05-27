import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as json_file:
        data_trades = json.load(json_file)

    profit_dict = {}
    total_profit = 0
    matecoin_account = 0

    for data_trade in data_trades:
        if data_trade["bought"] is None:
            bought_value = 0
        else:
            bought_value = (decimal.Decimal(data_trade["bought"])
                            * decimal.Decimal(data_trade["matecoin_price"]))

        if data_trade["sold"] is None:
            sold_value = 0
        else:
            sold_value = (decimal.Decimal(data_trade["sold"])
                          * decimal.Decimal(data_trade["matecoin_price"]))

        if data_trade["bought"] is None:
            bought_value_matecoin = 0
        else:
            bought_value_matecoin = decimal.Decimal(data_trade["bought"])
        if data_trade["sold"] is None:
            sold_value_matecoin = 0
        else:
            sold_value_matecoin = decimal.Decimal(data_trade["sold"])

        profit = sold_value - bought_value
        total_profit = total_profit + profit

        balance_matecoin = bought_value_matecoin - sold_value_matecoin
        matecoin_account = matecoin_account + balance_matecoin

    profit_dict["earned_money"] = str(total_profit)
    profit_dict["matecoin_account"] = str(matecoin_account)

    with open("profit.json", "w") as json_file:
        json.dump(profit_dict, json_file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
