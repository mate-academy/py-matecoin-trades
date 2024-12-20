import decimal
import json


def calculate_profit(name_file: str = "trades.json") -> None:
    dollars_to_bought = 0
    dollars_to_sold = 0
    coins = 0
    with open(name_file, "r") as f:
        list_json_file = json.load(f)
        for transaction in list_json_file:
            if transaction["sold"] is not None \
                    and transaction["bought"] is not None:
                coins += (decimal.Decimal(transaction["bought"])
                          - decimal.Decimal(transaction["sold"]))
                dollars_to_bought += \
                    (decimal.Decimal(transaction["bought"])
                     * decimal.Decimal(transaction["matecoin_price"]))
                dollars_to_sold += \
                    (decimal.Decimal(transaction["sold"])
                     * decimal.Decimal(transaction["matecoin_price"]))
            else:
                if transaction["sold"] is None:
                    coins += decimal.Decimal(transaction["bought"])
                    dollars_to_bought += \
                        (decimal.Decimal(transaction["bought"])
                         * decimal.Decimal(transaction["matecoin_price"]))
                else:
                    coins -= decimal.Decimal(transaction["sold"])
                    dollars_to_sold += \
                        (decimal.Decimal(transaction["sold"])
                         * decimal.Decimal(transaction["matecoin_price"]))

    profit_coin = {"earned_money": str(dollars_to_sold - dollars_to_bought),
                   "matecoin_account": str(coins)}
    with open("profit.json", "w") as file:
        json.dump(profit_coin, file, indent=2)
    print(profit_coin)
