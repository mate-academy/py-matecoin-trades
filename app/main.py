from decimal import Decimal
import json


def calculate_profit(filename: str) -> None:
    coin_bought = []
    coin_sold = []
    sum_price_bought = []
    sum_price_sold = []

    with open(filename, "r") as read_file:
        data = json.load(read_file)

    for dat in data:

        if dat["bought"] is not None:
            coins = Decimal(dat.get("bought"))
            price = Decimal(dat.get("matecoin_price"))

            got = coins * price
            sum_price_bought.append(got)
            coin_bought.append(coins)

        if dat["sold"] is not None:
            sale = Decimal(dat.get("sold"))
            price = Decimal(dat.get("matecoin_price"))

            earned = sale * price

            coin_sold.append(sale)
            sum_price_sold.append(earned)

    dollars = str(sum(sum_price_sold) - sum(sum_price_bought))
    remain = str(sum(coin_bought) - sum(coin_sold))

    mate_dict = {
        "earned_money": dollars,
        "matecoin_account": remain
    }

    with open("profit.json", "w") as f:
        json.dump(mate_dict, f, indent=2)
