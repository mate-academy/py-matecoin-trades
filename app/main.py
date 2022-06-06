import json
from decimal import Decimal, getcontext


class Trades:
    earned_money = Decimal(0)
    matecoin_account = Decimal(0)

    def __init__(self, bought: str, sold: str, matecoin_price: str):
        self.bought = bought
        self.sold = sold
        self.matecoin_price = matecoin_price
        if self.bought:
            self.earned_money -= Decimal(self.bought) * Decimal(
                self.matecoin_price)
            self.matecoin_account += Decimal(self.bought)
        if self.sold:
            self.earned_money += Decimal(self.sold) * Decimal(
                self.matecoin_price)
            self.matecoin_account -= Decimal(self.sold)


def calculate_profit(file_name: str):
    getcontext().prec = 8
    trades_stat_dict = {"earned_money": 0,
                        "matecoin_account": 0}
    trades_stat_list = []
    with open(file_name, "r") as f:
        for operation in json.load(f):
            trades_stat_list.append(Trades(operation["bought"],
                                           operation["sold"],
                                           operation["matecoin_price"]))
            trades_stat_dict["earned_money"] += trades_stat_list[
                -1].earned_money
            trades_stat_dict["matecoin_account"] += trades_stat_list[
                -1].matecoin_account

    trades_stat_dict["earned_money"] = str(trades_stat_dict["earned_money"])
    trades_stat_dict["matecoin_account"] = str(
        trades_stat_dict["matecoin_account"])

    with open("profit.json", "w") as f:
        json.dump(trades_stat_dict, f, indent=2)
