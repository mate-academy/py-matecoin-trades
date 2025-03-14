import json
from decimal import Decimal


def calculate_profit(trade_file_name: str) -> None:
    with open(trade_file_name, "r") as trade_f:
        trades_list = json.load(trade_f)

    profit_dict = {
        "earned_money": Decimal("0"),
        "matecoin_account": Decimal("0")
    }

    for dict_elem in trades_list:
        sold_amount = (
            Decimal(dict_elem["sold"])
            if dict_elem.get("sold") is not None
            else Decimal("0")
        )
        bought_amount = (
            Decimal(dict_elem["bought"])
            if dict_elem.get("bought") is not None
            else Decimal("0")
        )
        matecoin_price = Decimal(dict_elem.get("matecoin_price"))

        profit_dict["earned_money"] += (
            (matecoin_price * sold_amount)
            - (matecoin_price * bought_amount)
        )
        profit_dict["matecoin_account"] += bought_amount - sold_amount

    with open(
            "D:\\Programming\\PythonCore\\py-matecoin-trades/profit.json",
            "w"
    ) as profit_f:
        json.dump(
            {
                "earned_money": str(profit_dict["earned_money"]),
                "matecoin_account": str(profit_dict["matecoin_account"]),
            },
            profit_f,
            indent=2
        )
