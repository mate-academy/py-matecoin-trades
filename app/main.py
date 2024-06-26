import json
from decimal import Decimal


def calculate_profit(name_file: str) -> None:
    matecoin_account_balance = Decimal(0)
    dict_json = {}

    with open(name_file) as file:
        list_trades = json.load(file)
        sold_metacoin_price = Decimal("0")
        dolars_bougth = Decimal("0")
        sold_all = Decimal("0")
        for i in range(len(list_trades)):
            if list_trades[i]["bought"] is not None:
                bougth_metacoin = Decimal(list_trades[i]["bought"])
            else:
                bougth_metacoin = Decimal("0")
            if list_trades[i]["sold"] is not None:
                sold_metacoin = Decimal(list_trades[i]["sold"])
            else:
                sold_metacoin = Decimal("0")
            sold_all += sold_metacoin
            matecoin_account_balance += bougth_metacoin
            matecoin_price = Decimal(f"{list_trades[i]["matecoin_price"]}")
            sold_metacoin_price += sold_metacoin * matecoin_price
            dolars_bougth += bougth_metacoin * matecoin_price
        balance = matecoin_account_balance - sold_all
        earned = sold_metacoin_price - dolars_bougth
        dict_json["earned_money"] = str(earned)
        dict_json["matecoin_account"] = str(balance)
        with open("profit.json", "w") as f:
            json.dump(dict_json, f, indent=2)


if __name__ == "__main__":
    calculate_profit("trades.json")
