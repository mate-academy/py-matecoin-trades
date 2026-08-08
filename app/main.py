import json
import decimal


def calculate_profit(file_name: str) -> None:
    with open(file_name, "r") as f:
        agreement = json.load(f)
    purchase = 0
    bought_coin = 0
    selling = 0
    sold_coin = 0

    profit = {
        "earned_money": 0,
        "matecoin_account": 0
    }

    for i in agreement:
        if i["bought"] is not None:
            bought_coin += decimal.Decimal(i["bought"])
            purchase += (decimal.Decimal(i["bought"])
                         * decimal.Decimal(i["matecoin_price"]))
        if i["sold"] is not None:
            sold_coin += decimal.Decimal(i["sold"])
            selling += (decimal.Decimal(i["sold"])
                        * decimal.Decimal(i["matecoin_price"]))

    profit["matecoin_account"] = str(bought_coin - sold_coin)
    profit["earned_money"] = str(selling - purchase)

    with open("profit.json", "w") as a:
        json.dump(profit, a, indent=2)
