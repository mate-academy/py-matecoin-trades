import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as file_pointer:
        trades = json.load(file_pointer)

    bought_in_dollars = 0
    sold_in_dollars = 0
    mate_coin = 0

    for transaction in trades:
        if transaction["bought"]:
            bought_in_dollars += decimal.Decimal(
                transaction["bought"]
            ) * decimal.Decimal(transaction["matecoin_price"])
            mate_coin += decimal.Decimal(transaction["bought"])
        if transaction["sold"]:
            sold_in_dollars += decimal.Decimal(
                transaction["sold"]
            ) * decimal.Decimal(transaction["matecoin_price"])
            mate_coin -= decimal.Decimal(transaction["sold"])

    account = {
        "earned_money": str(sold_in_dollars - bought_in_dollars),
        "matecoin_account": str(mate_coin),
    }

    with open("profit.json", "w") as file_pointer:
        json.dump(account, file_pointer, indent=2)
