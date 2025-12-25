import json
import decimal


def calculate_profit(filename: str = "trades.json") -> None:
    with open(filename, "r") as file:
        data = json.load(file)
    earned_money = 0
    account_balance = 0
    for trade in data:
        if trade["bought"] is None:
            trade["bought"] = 0
        if trade["sold"] is None:
            trade["sold"] = 0

        earned_money += decimal.Decimal(trade["sold"]) * \
            decimal.Decimal(trade["matecoin_price"])\
            - decimal.Decimal(trade["bought"]) * \
            decimal.Decimal(trade["matecoin_price"])
        account_balance += decimal.Decimal(trade["bought"]) \
            - decimal.Decimal(trade["sold"])
    profit_dict = {
        "earned_money": str(earned_money),
        "matecoin_account": str(account_balance)}
    with open("profit.json", "w") as file_out:
        json.dump(profit_dict, file_out, indent=2)
