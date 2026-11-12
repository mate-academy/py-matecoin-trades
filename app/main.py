from decimal import Decimal
import json
from typing import TextIO


def calculate_profit(trade_info: TextIO) -> None:
    with open(trade_info, "r") as file:
        trade_data = json.load(file)
    bought = Decimal(0)
    sold = Decimal(0)
    volume_increase = Decimal(0)
    volume_decrease = Decimal(0)
    for data in trade_data:
        if data["sold"] is None:
            daily_bought = \
                (Decimal(data["bought"]) * Decimal(data["matecoin_price"]))
            bought += daily_bought
            daily_increase = Decimal(data["bought"])
            volume_increase += daily_increase
        elif data["bought"] is None:
            daily_sold = \
                (Decimal(data["sold"]) * Decimal(data["matecoin_price"]))
            sold += daily_sold
            daily_decrease = Decimal(data["sold"])
            volume_decrease += daily_decrease
        else:
            daily_bought = \
                (Decimal(data["bought"]) * Decimal(data["matecoin_price"]))
            bought += daily_bought
            daily_increase = Decimal(data["bought"])
            volume_increase += daily_increase
            daily_sold = \
                (Decimal(data["sold"]) * Decimal(data["matecoin_price"]))
            sold += daily_sold
            daily_decrease = Decimal(data["sold"])
            volume_decrease += daily_decrease
    profit = sold - bought
    matecoin_volume = volume_increase - volume_decrease
    trades = {"earned_money": str(profit),
              "matecoin_account": str(matecoin_volume)}
    with open("profit.json", "w") as file:
        json.dump(trades, file, indent=2)
