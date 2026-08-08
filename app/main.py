from decimal import Decimal
import json


def calculate_profit(name_file):
    with open(name_file, "r") as trades_file,\
         open("profit.json", "w") as profit_file:
        trades = json.load(trades_file)
        profit = {"earned_money": "0", "matecoin_account": "0"}
        for trade in trades:
            d = trade["matecoin_price"]
            if trade["bought"] is not None:
                matecoin = profit["matecoin_account"]
                emoney = profit["earned_money"]
                bght = trade["bought"]
                coin = str(Decimal(matecoin) + Decimal(bght))
                profit["matecoin_account"] = coin
                money = str(Decimal(emoney) - Decimal(d) * Decimal(bght))
                profit["earned_money"] = money
            if trade["sold"] is not None:
                matecoin = profit["matecoin_account"]
                emoney = profit["earned_money"]
                sld = trade["sold"]
                res_coin = str(Decimal(matecoin) - Decimal(sld))
                profit["matecoin_account"] = res_coin
                res_money = str(Decimal(emoney) + Decimal(d) * Decimal(sld))
                profit["earned_money"] = res_money
        json.dump(profit, profit_file, indent=2)
