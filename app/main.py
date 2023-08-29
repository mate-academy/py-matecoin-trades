import json

import decimal


def calculate_profit(name_of_file: str) -> None:
    with open(name_of_file, "r") as trades_file:
        trades = json.load(trades_file)

    output = 0
    mate_coin = 0

    for action in trades:
        if action["bought"]:
            output -= decimal.Decimal(action["bought"]) * \
                decimal.Decimal(action["matecoin_price"])
            mate_coin += decimal.Decimal(action["bought"])
        if action["sold"]:
            output += decimal.Decimal(action["sold"]) * \
                decimal.Decimal(action["matecoin_price"])
            mate_coin -= decimal.Decimal(action["sold"])

    current_coin_account = {
        "earned_money": str(output),
        "matecoin_account": str(mate_coin)
    }

    with open("../profit.json", "w") as profit:
        json.dump(current_coin_account, profit, indent=2)
