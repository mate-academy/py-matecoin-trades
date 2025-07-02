import json
from decimal import Decimal


def calculate_profit(
        file_name: str
) -> None:
    profit_dict = {}
    matecoin_amount = Decimal("0")
    bought_amount = Decimal("0")
    sold_amount = Decimal("0")
    with open(file_name, "r") as trades_file:
        trades_dict = json.load(trades_file)
        for trade in trades_dict:
            if trade["bought"] is not None:
                bought_amount += (Decimal(trade["bought"])
                                  * Decimal(trade["matecoin_price"]))
                matecoin_amount += Decimal(trade["bought"])
            if trade["sold"] is not None:
                sold_amount += (Decimal(trade["sold"])
                                * Decimal(trade["matecoin_price"]))
                matecoin_amount -= Decimal(trade["sold"])
        profit_dict["earned_money"] = str(sold_amount - bought_amount)
        profit_dict["matecoin_account"] = str(matecoin_amount)
    with open("profit.json", "w") as profit_file:
        json.dump(profit_dict, profit_file, indent=2)
