import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file:
        trading_data = json.load(file)
    matecoin_coins = decimal.Decimal("0.0")
    profit = decimal.Decimal("0.0")
    result_dict = {}
    for trade in trading_data:
        bought = 0
        sold = 0
        matecoin_price = decimal.Decimal(trade["matecoin_price"])
        if trade["bought"]:
            bought = decimal.Decimal(trade["bought"])
        if trade["sold"]:
            sold = decimal.Decimal(trade["sold"])
        profit += -(bought * matecoin_price) + (sold * matecoin_price)
        matecoin_coins += bought - sold
    result_dict["earned_money"] = str(profit)
    result_dict["matecoin_account"] = str(matecoin_coins)
    with open("profit.json", "w") as file:
        json.dump(result_dict, file, indent=2)
