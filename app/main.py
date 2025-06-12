from typing import Union, Any
import json
import os
from decimal import Decimal, getcontext
from pathlib import Path


getcontext().prec = 28


def load_json(json_file_name: str = "trades.json") -> Union[Any, None]:
    try:
        if isinstance(json_file_name, list):
            return json_file_name

        if isinstance(json_file_name, str) and Path(json_file_name).is_file():
            if os.path.getsize(json_file_name) != 0:
                with open(json_file_name, "r", encoding="utf-8") as f:
                    trade_data = json.load(f)
                    return trade_data
    except FileNotFoundError as fnf:
        print("File not found!", fnf)
    except json.JSONDecodeError as jde:
        print("JSON decode error!", jde)


def calculate_profit(trade_data: Union[str, list]) -> None:
    if isinstance(trade_data, str):
        trade_data = load_json(trade_data)

    trade_dict = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    for trade_day in trade_data:
        if trade_day["bought"] is not None:
            bought_trade = Decimal(
                trade_day["bought"]
            ) * Decimal(
                trade_day["matecoin_price"]
            )
            trade_dict["matecoin_account"] = Decimal(
                trade_dict["matecoin_account"]
            ) + Decimal(
                trade_day["bought"]
            )
            trade_dict["earned_money"] = Decimal(
                trade_dict["earned_money"]
            ) - Decimal(bought_trade)
        if trade_day["sold"] is not None:
            sold_trade = Decimal(
                trade_day["sold"]
            ) * Decimal(trade_day["matecoin_price"])
            trade_dict["earned_money"] = Decimal(
                trade_dict["earned_money"]
            ) + Decimal(sold_trade)
            trade_dict["matecoin_account"] = (
                trade_dict["matecoin_account"] - Decimal(trade_day["sold"])
            )

    if len(trade_dict) > 0:
        trade_dict = {
            "earned_money": str(trade_dict["earned_money"]),
            "matecoin_account": str(trade_dict["matecoin_account"])
        }
        with open("profit.json", "w") as f:
            json.dump(trade_dict, f, indent=2)


if __name__ == "__main__":
    data = load_json("trades.json")
    if data:
        profit = calculate_profit(data)
        if profit:
            print("Profit successfully calculated and written to profit.json")
    else:
        print("No data to process.")
