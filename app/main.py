import json
from decimal import Decimal


def calculate_profit(trade_file_path: str) -> None:
    with open(trade_file_path, "r") as trade_file:
        with open("profit.json", "w") as profit_file:
            trade_data = json.load(trade_file)
            net_profit_in_dollars = 0
            total_hold_matecoins = 0

            for trade in trade_data:
                if trade["bought"]:
                    net_profit_in_dollars -= (
                        Decimal(trade["bought"])
                        * Decimal(trade["matecoin_price"])
                    )
                    total_hold_matecoins += Decimal(trade["bought"])
                if trade["sold"]:
                    net_profit_in_dollars += (
                        Decimal(trade["sold"])
                        * Decimal(trade["matecoin_price"])
                    )
                    total_hold_matecoins -= Decimal(trade["sold"])

            profit_summary = {
                "earned_money": f"{net_profit_in_dollars}",
                "matecoin_account": f"{total_hold_matecoins}"
            }
            json.dump(profit_summary, profit_file, indent=2)
