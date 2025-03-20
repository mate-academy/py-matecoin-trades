import json
from decimal import Decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as trades_data_file:
        trades_data = json.load(trades_data_file)
        usd_wallet = Decimal("0")
        coin_wallet = Decimal("0")
        for transaction in trades_data:
            if transaction["bought"]:
                coin_wallet += Decimal(transaction["bought"])
                usd_wallet -= (
                    Decimal(transaction["bought"])
                    * Decimal(transaction["matecoin_price"])
                )
            if transaction["sold"]:
                coin_wallet -= Decimal(transaction["sold"])
                usd_wallet += (
                    Decimal(transaction["sold"])
                    * Decimal(transaction["matecoin_price"])
                )
        result = {
            "earned_money": str(usd_wallet),
            "matecoin_account": str(coin_wallet)
        }
        with open("profit.json", "w") as result_file:
            json.dump(result, result_file, indent=2)
