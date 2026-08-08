import json
from decimal import Decimal


def calculate_profit(file_json: str) -> None:
    with open(file_json) as trades_file:
        info = json.load(trades_file)
    matecoin = 0
    profit = 0
    for transaction in info:
        price = Decimal(transaction["matecoin_price"])
        if transaction.get("sold") is None:
            profit -= price * Decimal(transaction["bought"])
            matecoin += Decimal(transaction["bought"])
        elif transaction.get("bought") is None:
            profit += price * Decimal(transaction["sold"])
            matecoin -= Decimal(transaction["sold"])
        else:
            profit -= price * Decimal(transaction["bought"])
            matecoin += Decimal(transaction["bought"])
            profit += price * Decimal(transaction["sold"])
            matecoin -= Decimal(transaction["sold"])

    profit_dict = ({"earned_money": str(Decimal(profit)),
                    "matecoin_account": str(Decimal(matecoin))})

    with open("profit.json", "w") as profit_file:
        json.dump(profit_dict, profit_file, indent=2)
