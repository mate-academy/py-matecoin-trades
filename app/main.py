import json
from decimal import Decimal


def calculate_profit(name_of_file: str) -> None:
    with open(name_of_file, "r") as trades:
        json_data = json.load(trades)

    earned_money = 0
    result = {}
    mate_coin_state = 0

    for trade in json_data:
        # print(trade["bought"])
        bought = trade["bought"]
        sold = trade["sold"]
        mate_coin = trade["matecoin_price"]
        kupiono = 0
        wydano = 0

        if bought is None:
            bought = 0
        else:
            bought = Decimal(bought)
            kupiono += Decimal(bought) * Decimal(mate_coin)
            earned_money -= kupiono
            mate_coin_state += Decimal(bought)
            result = {"earned_money": str(earned_money),
                      "matecoin_account": str(mate_coin_state)}
        if sold is None:
            sold = 0
        else:
            sold = Decimal(sold)
            wydano += Decimal(sold) * Decimal(mate_coin)
            earned_money += wydano
            mate_coin_state -= Decimal(sold)
            result = {"earned_money": str(earned_money),
                      "matecoin_account" : str(mate_coin_state)}

    with open("profit.json", "w") as file:
        json.dump(result, file, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
