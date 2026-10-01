import json
from decimal import Decimal


def calculate_profit(trades_file: str) -> None:
    result_dict = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }
    with (open(trades_file, "r") as file_in,
          open("profit.json", "w") as file_out):
        content = json.load(file_in)
        for trade in content:
            if trade["bought"] is not None:
                bought = trade["bought"]
                matecoin_price = trade["matecoin_price"]
                trade_result = Decimal(bought) * Decimal(matecoin_price)
                result_dict["earned_money"] -= Decimal(f"{trade_result}")
                result_dict["matecoin_account"] += Decimal(trade["bought"])
            if trade["sold"] is not None:
                sold = trade["sold"]
                matecoin_price = trade["matecoin_price"]
                trade_result = Decimal(sold) * Decimal(matecoin_price)
                result_dict["earned_money"] += Decimal(f"{trade_result}")
                result_dict["matecoin_account"] -= Decimal(trade["sold"])
        result_dict["earned_money"] = str(result_dict["earned_money"])
        result_dict["matecoin_account"] = str(result_dict["matecoin_account"])
        json.dump(result_dict, file_out, indent=2)
        return
