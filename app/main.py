import json
from decimal import Decimal


def calculate_profit(json_file_name: str) -> None:
    earned_money = Decimal("0.0")
    matecoin_account = Decimal("0.0")

    with open(json_file_name, "r") as json_file:
        data = json.load(json_file)
        for transaction in data:
            matecoin_price = Decimal(transaction["matecoin_price"])
            if transaction["bought"]:
                bought_amount = Decimal(transaction["bought"])
                earned_money -= matecoin_price * bought_amount
                matecoin_account += bought_amount
            if transaction["sold"]:
                sold_amount = Decimal(transaction["sold"])
                earned_money += matecoin_price * sold_amount
                matecoin_account -= sold_amount

    profit_data = {
        "earned_money": str(earned_money),
        "matecoin_account": str(matecoin_account)

    }

    with open("profit.json", "w") as json_file:
        json.dump(profit_data, json_file, indent=2)


# Example usage
if __name__ == "__main__":
    calculate_profit("trades.json")
