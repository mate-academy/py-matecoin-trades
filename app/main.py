import json
import decimal


def calculate_profit(file_name: str) -> dict:
    earned_money = 0
    matecoin_account = 0

    with open(file_name, "r") as trades:
        trades_on_dict = json.load(trades)

        for trade in trades_on_dict:
            if trade["bought"]:
                earned_money -= decimal.Decimal(trade["matecoin_price"]) * decimal.Decimal(trade["bought"])  # noqa
                matecoin_account += decimal.Decimal(trade["bought"])
            if trade["sold"]:
                earned_money += decimal.Decimal(trade["matecoin_price"]) * decimal.Decimal(trade["sold"])  # noqa
                matecoin_account -= decimal.Decimal(trade["sold"])

    with open("profit.json", "w") as profit:
        profit_dict = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }
        json.dump(profit_dict, profit, indent=2)
