import json
from decimal import Decimal
import os


def calculate_profit(file_name: str = "trades.json") -> None:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    trades_file_path = os.path.join(current_dir, file_name)

    project_root_dir = os.path.dirname(current_dir)

    profit_file_path_app = os.path.join(current_dir, "profit.json")
    profit_file_path_project = os.path.join(project_root_dir, "profit.json")

    with open(trades_file_path, "r") as json_file:
        trades = json.load(json_file)

        matecoin_account = Decimal("0")
        earned_money = Decimal("0")

        for trade in trades:
            matecoin_price = Decimal(trade["matecoin_price"])
            if trade["bought"]:
                volume_bought = Decimal(trade["bought"])
                cost = volume_bought * matecoin_price
                earned_money -= cost
                matecoin_account += volume_bought
            if trade["sold"]:
                volume_sold = Decimal(trade["sold"])
                revenue = volume_sold * matecoin_price
                earned_money += revenue
                matecoin_account -= volume_sold

        result = {
            "earned_money": str(earned_money),
            "matecoin_account": str(matecoin_account)
        }

        with open(profit_file_path_app, "w") as json_file:
            json.dump(result, json_file, indent=2, sort_keys=True)
        with open(profit_file_path_project, "w") as json_file:
            json.dump(result, json_file, indent=2, sort_keys=True)
